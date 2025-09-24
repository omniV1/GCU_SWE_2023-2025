class BibleManager {
    constructor() {
        this.initializeSelectors();
        this.attachEventListeners();
        this.loadInitialData();
    }

    initializeSelectors() {
        this.versionSelect = document.getElementById('bibleVersion');
        this.bookSelect = document.getElementById('bibleBook');
        this.chapterSelect = document.getElementById('bibleChapter');
        this.versesContainer = document.getElementById('verses');
        this.crossReferencesContainer = document.getElementById('crossReferences');
    }

    attachEventListeners() {
        this.bookSelect.addEventListener('change', () => this.handleBookChange());
        this.chapterSelect.addEventListener('change', () => this.handleChapterChange());
    }

    loadInitialData() {
        this.loadBibleVersions();
        this.loadBibleBooks();
    }

    async loadBibleVersions() {
        try {
            const response = await fetch('/api/bible/versions');
            const versions = await response.json();
            this.populateVersionSelect(versions);
        } catch (error) {
            console.error('Error loading Bible versions:', error);
        }
    }

    async loadBibleBooks() {
        try {
            const response = await fetch('/api/bible/books');
            const books = await response.json();
            this.populateBookSelect(books);
        } catch (error) {
            console.error('Error loading Bible books:', error);
        }
    }

    populateVersionSelect(versions) {
        this.versionSelect.innerHTML = '<option value="">Select a version...</option>';
        versions.forEach(version => {
            const option = document.createElement('option');
            option.value = version.abbreviation;
            option.textContent = version.version;
            this.versionSelect.appendChild(option);
        });
    }

    populateBookSelect(books) {
        this.bookSelect.innerHTML = '<option value="">Select a book...</option>';
        books.forEach(book => {
            const option = document.createElement('option');
            option.value = book.id;
            option.textContent = book.name;
            this.bookSelect.appendChild(option);
        });
    }

    async handleBookChange() {
        const bookId = this.bookSelect.value;
        const version = this.versionSelect.value;

        if (!bookId || !version) {
            this.chapterSelect.innerHTML = '<option value="">Select a chapter...</option>';
            return;
        }

        try {
            // Fetch the chapter count from the API using the updated endpoint
            const response = await fetch(`/Bible/GetChapterCountJson/${version}/${bookId}`);
            const data = await response.json();

            // Clear and reset chapter select
            this.chapterSelect.innerHTML = '<option value="">Select a chapter...</option>';

            // Populate chapters based on the actual count
            for (let i = 1; i <= data.count; i++) {
                const option = document.createElement('option');
                option.value = i;
                option.textContent = `Chapter ${i}`;
                this.chapterSelect.appendChild(option);
            }
        } catch (error) {
            console.error('Error fetching chapter count:', error);
            this.chapterSelect.innerHTML = '<option value="">Error loading chapters</option>';
        }
    }

    async handleChapterChange() {
        const version = this.versionSelect.value;
        const book = this.bookSelect.value;
        const chapter = this.chapterSelect.value;

        if (!version || !book || !chapter) return;

        try {
            const response = await fetch(`/api/bible/${version}/${book}/${chapter}`);
            const verses = await response.json();
            this.displayVerses(verses);
        } catch (error) {
            console.error('Error loading verses:', error);
        }
    }

    displayVerses(verses) {
        this.versesContainer.innerHTML = '';
        verses.forEach(verse => {
            const verseDiv = document.createElement('div');
            verseDiv.className = 'verse mb-2';
            verseDiv.innerHTML = `<sup class="text-sm text-blue-600">${verse.verse}</sup> ${verse.text}`;
            verseDiv.addEventListener('click', () => this.loadCrossReferences(verse.id));
            this.versesContainer.appendChild(verseDiv);
        });
    }

    async loadCrossReferences(verseId) {
        try {
            const response = await fetch(`/api/bible/crossreferences/${verseId}`);
            const references = await response.json();
            this.displayCrossReferences(references);
        } catch (error) {
            console.error('Error loading cross references:', error);
        }
    }

    displayCrossReferences(references) {
        if (references.length === 0) {
            this.crossReferencesContainer.classList.add('hidden');
            return;
        }

        this.crossReferencesContainer.classList.remove('hidden');
        const referenceList = document.getElementById('crossReferenceList');
        referenceList.innerHTML = '';

        references.forEach(reference => {
            const referenceDiv = document.createElement('div');
            referenceDiv.className = 'cross-reference p-2 hover:bg-gray-100 rounded';
            referenceDiv.textContent = reference.sourceVerse;
            referenceList.appendChild(referenceDiv);
        });
    }
}

// Initialize the Bible manager when the DOM is loaded
document.addEventListener('DOMContentLoaded', () => {
    window.bibleManager = new BibleManager();
});