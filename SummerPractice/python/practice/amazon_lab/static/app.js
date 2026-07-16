/* Amazon Lab — NeetCode-style frontend */
const STORE = "amazon-lab-progress-v3";
const CODE_STORE = "amazon-lab-code-v3";
const LEGACY_STORE = "amazon-lab-progress-v2";

let BANK = null;
let pyodide = null;
let currentId = null;
let descTab = "pattern";
let timerSecs = 35 * 60;
let timerId = null;
let filterCat = null;
let saveFlashTimer = null;

const $ = (id) => document.getElementById(id);

function normalizeProgress(raw) {
  if (raw && raw.version === 3 && raw.byId) return raw;
  const byId = {};
  if (raw && typeof raw === "object") {
    for (const [id, val] of Object.entries(raw)) {
      if (id === "version" || id === "byId" || id === "meta") continue;
      if (typeof val === "string") {
        byId[id] = {
          status: val,
          attempts: val === "pass" || val === "fail" ? 1 : 0,
          lastVisit: Date.now(),
          note: "",
          mastered: val === "pass",
        };
      }
    }
  }
  return { version: 3, lastProblemId: null, lastView: "roadmap", byId };
}

function loadProgress() {
  try {
    let raw = JSON.parse(localStorage.getItem(STORE) || "null");
    if (!raw) {
      const leg = JSON.parse(localStorage.getItem(LEGACY_STORE) || "null");
      if (leg) raw = leg;
    }
    return normalizeProgress(raw);
  } catch {
    return normalizeProgress(null);
  }
}

function saveProgress(prog) {
  prog.version = 3;
  localStorage.setItem(STORE, JSON.stringify(prog));
  flashSaved();
}

function flashSaved() {
  const el = $("save-indicator");
  if (!el) return;
  el.textContent = "Saved locally ✓";
  el.classList.add("flash");
  clearTimeout(saveFlashTimer);
  saveFlashTimer = setTimeout(() => {
    el.classList.remove("flash");
    el.textContent = "Saved locally";
  }, 1500);
}

function probRec(id) {
  const p = loadProgress();
  if (!p.byId[id]) {
    p.byId[id] = { status: null, attempts: 0, lastVisit: null, note: "", mastered: false };
  }
  return p.byId[id];
}

function getStatus(id) {
  return probRec(id).status || null;
}

function patchProblem(id, patch) {
  const p = loadProgress();
  p.byId[id] = { ...probRec(id), ...patch, lastVisit: Date.now() };
  saveProgress(p);
}

function loadCodeMap() {
  try { return JSON.parse(localStorage.getItem(CODE_STORE) || "{}"); } catch { return {}; }
}
function saveCodeMap(m) {
  localStorage.setItem(CODE_STORE, JSON.stringify(m));
  flashSaved();
}
function esc(s) {
  return String(s).replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;");
}
function problemById(id) { return BANK.problems.find((p) => p.id === id); }

async function boot() {
  const res = await fetch("/data/problems.json");
  BANK = await res.json();
  $("bank-meta").textContent =
    `${BANK.meta.count} problems · ${BANK.meta.codeWalks || 0} code walks · goal ${BANK.meta.goal}`;
  updateProgress();
  renderRoadmap();
  renderPatternPicker();
  renderSidebar();
  await ensurePy().catch((e) => {
    $("status").textContent = "Python failed — check network";
    $("results").innerHTML = `<span class="err">${esc(e.message || e)}</span>`;
  });
  const prog = loadProgress();
  if (prog.lastProblemId && problemById(prog.lastProblemId)) {
    setView(prog.lastView || "practice");
    selectProblem(prog.lastProblemId, true);
  }
}

function statusIcon(id) {
  const r = probRec(id);
  if (r.mastered) return "★";
  if (r.status === "pass") return "✓";
  if (r.status === "fail") return "✗";
  if (r.attempts > 0 || r.note || loadCodeMap()[id]) return "◐";
  return "·";
}

function updateProgress() {
  const prog = loadProgress();
  const ids = BANK.problems.map((p) => p.id);
  const passed = ids.filter((id) => getStatus(id) === "pass").length;
  const started = ids.filter((id) => {
    const r = prog.byId[id];
    return r && (r.attempts > 0 || r.note || loadCodeMap()[id]) && r.status !== "pass";
  }).length;
  const mastered = ids.filter((id) => prog.byId[id]?.mastered).length;
  $("progress").textContent = `${passed} solved · ${started} in progress${mastered ? ` · ${mastered} mastered` : ""}`;
}

function renderRoadmap() {
  const root = $("roadmap-grid");
  root.innerHTML = "";
  const prog = loadProgress();
  for (const cat of BANK.roadmap) {
    const probs = BANK.problems.filter((p) => p.category === cat.id);
    if (!probs.length) continue;
    const done = probs.filter((p) => getStatus(p.id) === "pass").length;
    const pct = Math.round((done / probs.length) * 100);
    const el = document.createElement("div");
    el.className = "cat";
    el.innerHTML = `
      <div class="cat-h">
        <h2>${esc(cat.title)}</h2>
        <div class="bar"><span style="width:${pct}%"></span></div>
        <span class="meta">${done}/${probs.length}</span>
      </div>
      <div class="plist"></div>`;
    const plist = el.querySelector(".plist");
    for (const p of probs) {
      const card = document.createElement("div");
      card.className = "pcard";
      const mark = getStatus(p.id) === "pass" ? "pass" : getStatus(p.id) === "fail" ? "fail" : probRec(p.id).mastered ? "star" : "";
      const icon = statusIcon(p.id);
      card.innerHTML = `<div class="row"><span class="st ${mark}">${icon}</span>
        <span>${esc(p.title)}</span>
        <span class="diff ${p.difficulty}">${esc(p.difficulty)}</span></div>
        <div class="meta" style="margin-top:4px;">${esc(p.pattern)}${p.lc ? " · LC " + p.lc : ""}</div>`;
      card.onclick = () => openPractice(p.id);
      plist.appendChild(card);
    }
    root.appendChild(el);
  }
}

function renderSidebar() {
  const root = $("sidebar");
  root.innerHTML = "";
  const prog = loadProgress();
  const cats = filterCat
    ? BANK.roadmap.filter((c) => c.id === filterCat)
    : BANK.roadmap;
  for (const cat of cats) {
    const probs = BANK.problems.filter((p) => p.category === cat.id);
    if (!probs.length) continue;
    const h = document.createElement("div");
    h.className = "side-h";
    h.textContent = cat.title;
    root.appendChild(h);
    for (const p of probs) {
      const row = document.createElement("div");
      row.className = "prob" + (p.id === currentId ? " active" : "");
      const icon = statusIcon(p.id);
      const mark = getStatus(p.id) || (probRec(p.id).mastered ? "star" : "");
      row.innerHTML = `<span class="st ${mark}">${icon}</span><span>${esc(p.title)}</span>`;
      row.onclick = () => selectProblem(p.id);
      root.appendChild(row);
    }
  }
}

function setView(name) {
  document.querySelectorAll(".tabbtn").forEach((b) => {
    b.classList.toggle("active", b.dataset.view === name);
  });
  $("view-roadmap").classList.toggle("hide", name !== "roadmap");
  $("view-picker").classList.toggle("hide", name !== "picker");
  $("view-practice").classList.toggle("hide", name !== "practice");
  const prog = loadProgress();
  prog.lastView = name;
  saveProgress(prog);
  if (name === "roadmap") renderRoadmap();
  if (name === "picker") renderPatternPicker();
}

function renderWhenBlock(w) {
  if (!w) return "";
  const signals = (w.signals || []).map((s) => `<li>${esc(s)}</li>`).join("");
  const not = (w.notThis || []).map((s) => `<li>${esc(s)}</li>`).join("");
  const heard = w.interviewHeard
    ? `<div class="when-heard"><b>When you hear:</b> &ldquo;${esc(w.interviewHeard)}&rdquo;</div>`
    : "";
  const real = w.realWorld
    ? `<div class="when-real"><b>Real-world hook:</b> ${esc(w.realWorld)}</div>`
    : "";
  const anchor = w.lcAnchor
    ? `<div class="when-anchor"><b>Anchor:</b> ${esc(w.lcAnchor)}</div>`
    : "";
  return `
    <div class="when-box">
      <div class="when-reach"><b>Reach for:</b> ${esc(w.reachFor || "")}</div>
      ${heard}
      ${real}
      ${anchor}
      ${signals ? `<div class="when-col"><b>Problem signals</b><ul>${signals}</ul></div>` : ""}
      ${not ? `<div class="when-col bad"><b>Usually NOT this pattern if</b><ul>${not}</ul></div>` : ""}
    </div>`;
}

function renderPatternPicker() {
  const root = $("picker-content");
  if (!root || !BANK.patternPicker) return;
  const pk = BANK.patternPicker;
  const steps = (pk.decisionSteps || [])
    .map(
      (s, i) =>
        `<div class="pick-step"><span class="pick-n">${i + 1}</span><div><strong>${esc(s.q)}</strong><div class="pick-ans yes">Yes → ${esc(s.yes)}</div>${s.no !== "next" ? `<div class="pick-ans no">No → ${esc(s.no)}</div>` : `<div class="pick-ans no">No → keep going</div>`}</div></div>`
    )
    .join("");
  const cats = (pk.categories || [])
    .map((c) => {
      const probs = BANK.problems.filter((p) => p.category === c.id);
      const use = (c.useWhen || []).map((x) => `<li>${esc(x)}</li>`).join("");
      const keys = (c.keywords || []).map((k) => `<span class="kw">${esc(k)}</span>`).join("");
      const not = (c.notWhen || []).map((x) => `<li>${esc(x)}</li>`).join("");
      const ask = (c.askYourself || []).map((x) => `<li>${esc(x)}</li>`).join("");
      return `
        <article class="pick-cat" id="cat-${esc(c.id)}">
          <header>
            <h2>${esc(c.title)}</h2>
            <p class="one-liner">${esc(c.oneLiner || "")}</p>
          </header>
          <div class="pick-grid">
            <div><h4>Use when</h4><ul>${use}</ul></div>
            <div><h4>Keywords in prompt</h4><div class="kw-row">${keys}</div></div>
            <div><h4>Ask yourself</h4><ul>${ask}</ul></div>
            <div class="warn"><h4>Pick something else if</h4><ul>${not}</ul></div>
          </div>
          <div class="pick-probs">${probs.slice(0, 6).map((p) => `<button type="button" class="pick-link" data-pid="${esc(p.id)}">${esc(p.title)}</button>`).join("")}${probs.length > 6 ? `<span class="meta">+${probs.length - 6} more in Practice</span>` : ""}</div>
        </article>`;
    })
    .join("");
  root.innerHTML = `
    <section class="pick-section">
      <h2>Quick decision flow (read top to bottom)</h2>
      <p class="prose muted">First matching "Yes" is your starting bucket. Then open a problem and check its signals.</p>
      <div class="pick-flow">${steps}</div>
    </section>
    <section class="pick-section">
      <h2>All patterns — signals cheat sheet</h2>
      ${cats}
    </section>`;
  root.querySelectorAll(".pick-link").forEach((btn) => {
    btn.onclick = () => openPractice(btn.dataset.pid);
  });
}

function openPractice(id) {
  filterCat = null;
  setView("practice");
  selectProblem(id);
}

function selectProblem(id, skipViewSwitch) {
  if (currentId) {
    saveCurrentCode();
    saveCurrentNote();
  }
  currentId = id;
  const p = problemById(id);
  const map = loadCodeMap();
  $("editor").value = map[id] || p.starter;
  $("fn-label").textContent = p.fn ? `Implement ${p.fn}(...)` : "";
  const rec = probRec(id);
  if ($("problem-note")) $("problem-note").value = rec.note || "";
  updateMasteredBtn();
  const prog = loadProgress();
  prog.lastProblemId = id;
  if (!skipViewSwitch) prog.lastView = "practice";
  saveProgress(prog);
  patchProblem(id, { attempts: (rec.attempts || 0) }); // touch lastVisit
  renderDesc(p);
  renderSidebar();
  const r = probRec(id);
  const statusLine = r.status === "pass"
    ? "Previously accepted — retype from memory or mark mastered."
    : r.attempts > 0
      ? `In progress (${r.attempts} submit${r.attempts > 1 ? "s" : ""}) — your code and notes are saved.`
      : "Learn pattern tab first, then code in the editor.";
  $("results").innerHTML = `<span class="muted">${statusLine}</span>`;
}

function saveCurrentCode() {
  if (!currentId) return;
  const map = loadCodeMap();
  map[currentId] = $("editor").value;
  saveCodeMap(map);
}

function saveCurrentNote() {
  if (!currentId || !$("problem-note")) return;
  patchProblem(currentId, { note: $("problem-note").value });
}

function updateMasteredBtn() {
  const btn = $("btn-mastered");
  if (!btn || !currentId) return;
  const m = probRec(currentId).mastered;
  btn.textContent = m ? "Mastered ★" : "Mark mastered";
  btn.classList.toggle("active", m);
}

function mdLite(text) {
  /* tiny markdown: `code` + paragraphs */
  const escaped = esc(text || "");
  return escaped
    .replace(/`([^`]+)`/g, "<code>$1</code>")
    .replace(/\*\*([^*]+)\*\*/g, "<strong>$1</strong>")
    .split(/\n\n+/)
    .map((para) => `<p>${para.replace(/\n/g, "<br>")}</p>`)
    .join("");
}

function renderExamples(examples) {
  if (!examples || !examples.length) {
    return `<p class="muted">No examples yet — use Learn pattern tab.</p>`;
  }
  return examples
    .map((ex, i) => {
      const mock = ex.mockup
        ? `<div class="mockup"><div class="mockup-label">Diagram</div><pre>${esc(ex.mockup)}</pre></div>`
        : "";
      return `
      <article class="example">
        <header>Example ${i + 1}:</header>
        <div class="io"><span class="k">Input:</span> <code>${esc(ex.input)}</code></div>
        <div class="io"><span class="k">Output:</span> <code>${esc(ex.output)}</code></div>
        <div class="io explain"><span class="k">Explanation:</span> ${esc(ex.explanation)}</div>
        ${mock}
      </article>`;
    })
    .join("");
}

function renderLineTable(lines) {
  if (!lines || !lines.length) return "";
  const rows = lines
    .map(
      (row, i) =>
        `<tr><td class="ln">${i + 1}</td><td class="lc"><code>${esc(row.code)}</code></td><td>${esc(row.meaning)}</td></tr>`
    )
    .join("");
  return `<table class="line-table"><thead><tr><th>#</th><th>Python line</th><th>What it does (plain English)</th></tr></thead><tbody>${rows}</tbody></table>`;
}

function renderTraceTable(trace) {
  if (!trace || !trace.length) return "";
  const rows = trace
    .map(
      (row) =>
        `<tr><td><code>${esc(row.step)}</code></td><td><code>${esc(row.vars)}</code></td><td>${esc(row.note || "")}</td></tr>`
    )
    .join("");
  return `<table class="line-table trace-table"><thead><tr><th>Step</th><th>Variables</th><th>What changed</th></tr></thead><tbody>${rows}</tbody></table>`;
}

function renderHintTable(hints) {
  if (!hints || !hints.length) return "";
  const rows = hints
    .map(
      (h) =>
        `<tr><td><code>${esc(h.where)}</code></td><td>${esc(h.job)}</td></tr>`
    )
    .join("");
  return `<table class="line-table hint-table"><thead><tr><th>Where</th><th>Your job (fill the template)</th></tr></thead><tbody>${rows}</tbody></table>`;
}

function renderPatternGuide(p) {
  const g = p.patternGuide || {};
  const algo = (g.algorithm || [])
    .map((step, i) => `<li><span class="algo-n">${i + 1}.</span> ${esc(step)}</li>`)
    .join("");
  const pitfalls = (g.pitfalls || [])
    .map((m) => `<li>${esc(m)}</li>`)
    .join("");
  return `
    <div class="title-row">
      <h1>${esc(p.title)}</h1>
      <span class="pill pattern">${esc(p.pattern)}</span>
    </div>
    <div class="callout warn"><b>When to use this move</b>${renderWhenBlock(g.whenToUse)}</div>
    ${p.id === "ah-two-sum" ? `<div class="callout info"><b>Return indices, not the numbers.</b> <code>[0, 1]</code> means <code>nums[0] + nums[1]</code>, <em>not</em> the values 0 and 1. Accepted output <code>[0,1]</code> on <code>[2,7,11,15], 9</code> because <code>2 + 7 = 9</code>.</div>` : ""}
    <div class="callout good"><b>NeetCode flow:</b> confirm pattern above → intuition → algorithm → fill template in editor.</div>
    <h3>Intuition</h3>
    <p class="prose">${mdLite(g.intuition || p.whatsNew)}</p>
    ${g.brute ? `<h3>Brute force</h3><p class="prose muted">${esc(g.brute)}</p>` : ""}
    <h3>Algorithm</h3>
    <ol class="algo-list">${algo}</ol>
    <h3>Code template (you fill the blanks)</h3>
    <div class="template-block"><pre>${esc(g.template || "# template coming soon")}</pre></div>
    <h3>What to write in each blank</h3>
    ${renderHintTable(g.hints)}
    <h3>Dry run — Example 1</h3>
    <p class="prose muted">Follow the state table, then simulate it yourself.</p>
    ${renderTraceTable(g.trace)}
    <div class="trace-bar">
      <button class="btn primary" id="btn-run-trace">Simulate Example 1</button>
      <span class="meta">Prints variable states — still not your submitted function.</span>
    </div>
    ${pitfalls ? `<h3>Watch out for</h3><ul class="mistake-list">${pitfalls}</ul>` : ""}
    ${g.complexity ? `<h3>Complexity</h3><p>${esc(g.complexity)}</p>` : ""}
    <div class="callout info"><b>Now you code:</b> use the editor starter on the right. Stuck 15+ min? Hint, then Solution — retype from memory after.</div>`;
}

function renderDesc(p) {
  const pane = $("desc-pane");
  if (descTab === "pattern") {
    pane.innerHTML = renderPatternGuide(p);
    const btn = $("btn-run-trace");
    if (btn) btn.onclick = () => runPatternTrace(p);
    return;
  }
  if (descTab === "bridge") {
    const firstMock = (p.examples || []).find((e) => e.mockup);
    pane.innerHTML = `
      <div class="title-row"><h1>Pattern bridge</h1><span class="pill pattern">${esc(p.pattern)}</span></div>
      <div class="callout info"><b>YOU ALREADY KNOW</b><br>${esc(p.alreadyKnow)}</div>
      <div class="callout good"><b>WHAT'S NEW</b><br>${esc(p.whatsNew)}</div>
      <h3>Trace</h3><pre class="trace">${esc(p.trace)}</pre>
      ${firstMock ? `<h3>Visualization</h3><div class="mockup"><pre>${esc(firstMock.mockup)}</pre></div>` : ""}
      <h3>Complexity</h3><p>${esc(p.complexity)}</p>`;
    return;
  }
  if (descTab === "interview") {
    pane.innerHTML = `
      <div class="title-row"><h1>Say this out loud</h1></div>
      <div class="say"><b>Script:</b> ${esc(p.sayOutLoud)}</div>
      <div class="callout bad">Amazon fail modes: silence, no edges, wrong Big-O, ego when nudged.</div>
      <div class="callout good">Score signals: clarify, name pattern, catch bugs, collaborate.</div>`;
    return;
  }
  pane.innerHTML = `
    <div class="title-row">
      <h1>${esc(p.title)}</h1>
      <span class="pill pattern">${esc(p.pattern)}</span>
      <span class="pill diff ${p.difficulty}">${esc(p.difficulty)}</span>
      ${p.lc ? `<span class="pill">LC ${p.lc}</span>` : ""}
    </div>
    <div class="prompt">${mdLite(p.prompt || p.whatsNew)}</div>
    <div class="callout info"><b>YOU ALREADY KNOW</b><br>${esc(p.alreadyKnow)}</div>
    <div class="callout good"><b>WHAT'S NEW</b><br>${esc(p.whatsNew)}</div>
    <h3>Examples</h3>
    <div class="examples">${renderExamples(p.examples)}</div>
    ${p.constraints ? `<h3>Constraints</h3><pre class="constraints">${esc(p.constraints)}</pre>` : ""}
    <h3>Complexity</h3><p>${esc(p.complexity)}</p>
    <div class="say"><b>Interview line:</b> ${esc(p.sayOutLoud)}</div>`;
}

async function ensurePy() {
  if (pyodide) return pyodide;
  $("status").textContent = "Loading Python…";
  $("btn-run").disabled = true;
  $("btn-submit").disabled = true;
  pyodide = await loadPyodide({ indexURL: "https://cdn.jsdelivr.net/pyodide/v0.26.4/full/" });
  $("status").textContent = "Python ready";
  $("btn-run").disabled = false;
  $("btn-submit").disabled = false;
  return pyodide;
}

function pyRepr(v) {
  return JSON.stringify(v);
}

function toJs(result) {
  let js = result;
  if (js && typeof js.toJs === "function") {
    js = js.toJs({ dict_converter: Object.fromEntries });
  }
  return js;
}

function normalizeGroups(groups) {
  return JSON.stringify(
    (groups || []).map((g) => [...g].sort()).sort((a, b) => JSON.stringify(a).localeCompare(JSON.stringify(b)))
  );
}

function indexPairEqual(got, expect) {
  if (!Array.isArray(got) || !Array.isArray(expect) || got.length !== 2 || expect.length !== 2) return false;
  return got[0] === expect[0] && got[1] === expect[1]
    || got[0] === expect[1] && got[1] === expect[0];
}

function fmtVal(v) {
  return esc(JSON.stringify(v));
}

/** Human-readable check showing WHY the answer works (or doesn't). */
function buildVerification(problemId, test, got, expect) {
  const lines = [];
  const args = test.args || [];

  if (problemId === "ah-two-sum" && Array.isArray(got) && got.length === 2 && Array.isArray(args[0])) {
    const nums = args[0];
    const target = args[1];
    const i = got[0];
    const j = got[1];
    if (typeof i === "number" && typeof j === "number" && i >= 0 && j >= 0 && i < nums.length && j < nums.length) {
      const sum = nums[i] + nums[j];
      lines.push(`Indices ${i} and ${j} → nums[${i}]+nums[${j}] = ${nums[i]}+${nums[j]} = ${sum}`);
      lines.push(target != null ? (sum === target ? `Matches target ${target}` : `Does NOT match target ${target}`) : "");
    } else if (typeof i === "number" && typeof j === "number") {
      lines.push(`Invalid indices [${i}, ${j}] for array of length ${nums.length}`);
    }
    if (got[0] < nums.length && got[1] < nums.length && nums.includes(got[0]) && nums.includes(got[1]) && got[0] !== 0 && got[1] !== 1) {
      lines.push("Tip: LeetCode wants indices [i,j], not the values at those positions.");
    }
    lines.push("Remember: return [index1, index2], not [nums[i], nums[j]].");
    return lines.filter(Boolean);
  }

  if (problemId === "tp-two-sum-ii" && Array.isArray(got) && got.length === 2 && Array.isArray(args[0])) {
    const nums = args[0];
    const target = args[1];
    const L = got[0] - 1;
    const R = got[1] - 1;
    if (L >= 0 && R < nums.length) {
      const sum = nums[L] + nums[R];
      lines.push(`1-indexed [${got[0]}, ${got[1]}] → nums[${L}]+nums[${R}] = ${nums[L]}+${nums[R]} = ${sum}`);
      lines.push(sum === target ? `Matches target ${target}` : `Does NOT match target ${target}`);
    }
    return lines;
  }

  if (problemId === "ah-contains-duplicate" && Array.isArray(args[0])) {
    const nums = args[0];
    const seen = new Set();
    let dup = null;
    for (const x of nums) {
      if (seen.has(x)) { dup = x; break; }
      seen.add(x);
    }
    const hasDup = dup != null;
    if (hasDup) {
      lines.push(`Duplicate in input: ${dup} appears more than once → correct answer is true`);
    } else {
      lines.push("All elements distinct → correct answer is false");
    }
    if (typeof got === "boolean" && typeof expect === "boolean" && got !== expect) {
      lines.push(`You returned ${got}, but expected ${expect}`);
    } else if (typeof got === "boolean" && got === expect) {
      lines.push(`Your return ${got} matches the input`);
    }
    return lines;
  }

  if (problemId === "sw-best-stock" && typeof got === "number" && Array.isArray(args[0])) {
    const prices = args[0];
    let minP = Infinity, best = 0;
    for (const p of prices) {
      minP = Math.min(minP, p);
      best = Math.max(best, p - minP);
    }
    lines.push(`Max profit buy-low-sell-later = ${best}`);
    lines.push(got === best ? "Your return matches max profit" : `Expected max profit ${best}`);
    return lines;
  }

  if (typeof got === "boolean" && typeof expect === "boolean") {
    lines.push(got ? "Returned True" : "Returned False");
    return lines;
  }

  if (typeof got === "number" && typeof expect === "number") {
    lines.push(`Numeric answer: ${got}`);
    if (got === expect) lines.push("Matches expected value");
    return lines;
  }

  if (Array.isArray(got) && Array.isArray(expect) && !test.expectGroups && !test.expectSet) {
    lines.push(`Returned array length ${got.length}, expected length ${expect.length}`);
    if (JSON.stringify(got) === JSON.stringify(expect)) {
      lines.push("Exact match with expected output");
    } else if (test.unorderedPair && indexPairEqual(got, expect)) {
      lines.push("Index pair matches (order allowed to differ)");
    }
    return lines;
  }

  if (got === expect || JSON.stringify(got) === JSON.stringify(expect)) {
    lines.push("Output matches expected");
  }
  return lines;
}

function renderTestCase(caseNum, callLabel, got, expect, ok, verification, errMsg) {
  const cls = ok ? "result-case ok" : "result-case fail";
  const icon = ok ? "✓" : "✗";
  const exp = expect !== undefined ? fmtVal(expect) : "—";
  const verify = (verification || [])
    .map((v) => `<div class="case-verify">${esc(v)}</div>`)
    .join("");
  return `
<div class="${cls}">
  <div class="case-head">${icon} Case ${caseNum}</div>
  ${callLabel ? `<div class="case-call">${esc(callLabel)}</div>` : ""}
  <div class="case-row"><span class="lbl">Returned</span><code>${got === null || got === undefined ? "—" : fmtVal(got)}</code></div>
  <div class="case-row"><span class="lbl">Expected</span><code>${exp}</code></div>
  ${verify}
  ${errMsg ? `<div class="case-extra">${errMsg}</div>` : ""}
</div>`;
}

async function runUserCode(extra = "") {
  const py = await ensurePy();
  let out = "";
  py.setStdout({ batched: (s) => { out += s + "\n"; } });
  py.setStderr({ batched: (s) => { out += "[stderr] " + s + "\n"; } });
  await py.runPythonAsync($("editor").value + "\n" + extra);
  return out;
}

async function submitTests() {
  const p = problemById(currentId);
  const box = $("results");
  box.innerHTML = `<span class="muted">Running…</span>`;
  try {
    await runUserCode("");
    const py = pyodide;
    let passed = 0;
    const blocks = [];
    for (let i = 0; i < p.tests.length; i++) {
      const t = p.tests[i];
      try {
        let js;
        let callLabel = "";
        let expect = t.expect;

        if (t.setup) {
          await py.runPythonAsync(t.setup);
          js = toJs(await py.runPythonAsync(t.call));
          callLabel = t.call || "(setup test)";
        } else {
          const args = t.deepcopy ? JSON.parse(JSON.stringify(t.args)) : t.args;
          callLabel = `${p.fn}(${args.map(pyRepr).join(", ")})`;
          js = toJs(await py.runPythonAsync(callLabel));
        }

        let ok = false;
        if (t.expectGroups) {
          ok = normalizeGroups(js) === normalizeGroups(t.expectGroups);
          expect = t.expectGroups;
        } else if (t.expectSet) {
          ok = Array.isArray(js) && t.expectSet.every((x) => js.includes(x))
            && new Set(js).size === new Set(t.expectSet).size;
          expect = t.expectSet;
        } else if (t.unorderedPair) {
          ok = indexPairEqual(js, t.expect);
        } else {
          ok = JSON.stringify(js) === JSON.stringify(t.expect);
        }

        const verification = buildVerification(p.id, t, js, expect);
        if (ok) passed++;

        blocks.push(renderTestCase(i + 1, callLabel, js, expect, ok, verification));
      } catch (e) {
        blocks.push(renderTestCase(i + 1, t.call || p.fn + "(...)", null, t.expect, false, [], esc(String(e.message || e))));
      }
    }
    const all = passed === p.tests.length;
    const summary = all
      ? `<div class="result-summary ok">Accepted — ${passed}/${p.tests.length}</div>`
      : `<div class="result-summary fail">Wrong Answer — ${passed}/${p.tests.length}</div>`;
    box.innerHTML = summary + blocks.join("");
    const rec = probRec(currentId);
    patchProblem(currentId, {
      status: all ? "pass" : "fail",
      attempts: (rec.attempts || 0) + 1,
      passedAt: all ? Date.now() : rec.passedAt,
    });
    updateProgress();
    renderSidebar();
    renderRoadmap();
    updateMasteredBtn();
  } catch (e) {
    box.innerHTML = `<span class="err">Runtime Error</span>\n${esc(e.message || e)}`;
    const rec = probRec(currentId);
    patchProblem(currentId, { status: "fail", attempts: (rec.attempts || 0) + 1 });
    updateProgress();
    renderSidebar();
  }
}

async function runPatternTrace(p) {
  const code = p.patternGuide && (p.patternGuide.demo || p.patternGuide.runnable);
  const box = $("results");
  if (!code) {
    box.innerHTML = `<span class="err">No simulation for this problem yet.</span>`;
    return;
  }
  box.innerHTML = `<span class="muted">Simulating Example 1…</span>`;
  try {
    const out = await runUserCode(code);
    box.innerHTML = `<span class="ok">Example 1 simulation (not your submission):</span>\n${esc(out || "(no output)")}`;
  } catch (e) {
    box.innerHTML = `<span class="err">Simulation error</span>\n${esc(e.message || e)}`;
  }
}

async function runOnly() {
  try {
    const out = await runUserCode(`\nprint("Loaded OK")\n`);
    $("results").innerHTML = `<span class="muted">Run:</span>\n${esc(out || "(no stdout)")}`;
  } catch (e) {
    $("results").innerHTML = `<span class="err">Runtime Error</span>\n${esc(e.message || e)}`;
  }
}

function nextProblem() {
  const idx = BANK.problems.findIndex((p) => p.id === currentId);
  if (idx >= 0 && idx < BANK.problems.length - 1) selectProblem(BANK.problems[idx + 1].id);
}

function tick() {
  const m = String(Math.floor(timerSecs / 60)).padStart(2, "0");
  const s = String(timerSecs % 60).padStart(2, "0");
  $("timer").textContent = `${m}:${s}`;
  if (timerSecs <= 0) {
    clearInterval(timerId);
    timerId = null;
    $("results").innerHTML += `\n<span class="err">Timer done — explain edges and complexity.</span>`;
    return;
  }
  timerSecs--;
}

/* events */
document.querySelectorAll(".tabbtn").forEach((b) => {
  b.addEventListener("click", () => setView(b.dataset.view));
});
document.querySelectorAll(".desc .tab").forEach((tab) => {
  tab.addEventListener("click", () => {
    document.querySelectorAll(".desc .tab").forEach((t) => t.classList.remove("active"));
    tab.classList.add("active");
    descTab = tab.dataset.pane;
    if (currentId) renderDesc(problemById(currentId));
  });
});
$("btn-run").onclick = runOnly;
$("btn-submit").onclick = submitTests;
$("btn-reset-code").onclick = () => {
  $("editor").value = problemById(currentId).starter;
};
$("btn-hint").onclick = () => {
  $("results").innerHTML = `<span class="muted">Hint:</span>\n${esc(problemById(currentId).hint)}`;
};
$("btn-solution").onclick = () => {
  if (!confirm("Reveal solution? Only after 15+ min stuck. Retype from memory after.")) return;
  $("editor").value = problemById(currentId).solution;
};
$("btn-next").onclick = nextProblem;
$("btn-reset").onclick = () => {
  if (!confirm("Reset ALL progress, notes, and saved code in this browser?")) return;
  localStorage.removeItem(STORE);
  localStorage.removeItem(CODE_STORE);
  localStorage.removeItem(LEGACY_STORE);
  location.reload();
};
$("btn-mastered").onclick = () => {
  if (!currentId) return;
  const rec = probRec(currentId);
  patchProblem(currentId, { mastered: !rec.mastered });
  updateMasteredBtn();
  updateProgress();
  renderSidebar();
  renderRoadmap();
};
$("btn-export").onclick = () => {
  const payload = {
    exported: new Date().toISOString(),
    progress: loadProgress(),
    code: loadCodeMap(),
  };
  const blob = new Blob([JSON.stringify(payload, null, 2)], { type: "application/json" });
  const a = document.createElement("a");
  a.href = URL.createObjectURL(blob);
  a.download = "amazon-lab-progress.json";
  a.click();
  URL.revokeObjectURL(a.href);
};
let codeSaveTimer = null;
let noteSaveTimer = null;
$("editor").addEventListener("input", () => {
  clearTimeout(codeSaveTimer);
  codeSaveTimer = setTimeout(saveCurrentCode, 400);
});
if ($("problem-note")) {
  $("problem-note").addEventListener("input", () => {
    clearTimeout(noteSaveTimer);
    noteSaveTimer = setTimeout(saveCurrentNote, 400);
  });
}
$("editor").addEventListener("keydown", (e) => {
  if (e.key === "Tab") {
    e.preventDefault();
    const ta = e.target;
    const start = ta.selectionStart;
    ta.value = ta.value.slice(0, start) + "    " + ta.value.slice(ta.selectionEnd);
    ta.selectionStart = ta.selectionEnd = start + 4;
  }
});

$("btn-protocol").onclick = () => $("protocol-modal").classList.add("show");
$("close-protocol").onclick = () => $("protocol-modal").classList.remove("show");
$("btn-timer").onclick = () => {
  if (timerId) { clearInterval(timerId); timerId = null; return; }
  timerSecs = 35 * 60;
  tick();
  timerId = setInterval(tick, 1000);
};

boot().catch((e) => {
  document.body.innerHTML = `<pre style="padding:24px;color:#f87171">Failed to load lab.
Make sure you ran: python serve.py
from the amazon_lab folder.

${e}</pre>`;
});
