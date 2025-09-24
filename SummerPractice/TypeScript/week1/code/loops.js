(function () {
    var scores = [85, 90, 78];
    for (var i = 0; i < scores.length; i++) {
        console.log("Score ".concat(i + 1, ": ").concat(scores[i]));
    }
    var count = 0;
    while (count < 3) {
        console.log("Count: ".concat(count));
        count++;
    }
    var languages = ["TypeScript", "Java", "CSharp"];
    for (var _i = 0, languages_1 = languages; _i < languages_1.length; _i++) {
        var lang = languages_1[_i];
        console.log(lang);
    }
    var person = { name: "Owen", age: 26 };
    for (var key in person) {
        console.log("".concat(key, ": ").concat(person[key]));
    }
})();
