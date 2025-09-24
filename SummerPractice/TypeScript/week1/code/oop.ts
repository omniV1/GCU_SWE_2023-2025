(() => {
    class Animal {
        constructor(private name: string) {}

        public getName(): string {
            return this.name;
        }

        public speak(): void {
            console.log(`${this.name} makes a sound.`);
        }
    }

    class Dog extends Animal {
        constructor(name: string, private breed: string) {
            super(name);
        }

        public getBreed(): string {
            return this.breed;
        }

        public speak(): void {
            console.log(`${this.getName()} barks.`);
        }
    }

    interface Pet {
        play(): void;
    }

    class Cat extends Animal implements Pet {
        public speak(): void {
            console.log(`${this.getName()} meows.`);
        }

        public play(): void {
            console.log(`${this.getName()} is playing.`);
        }
    }

    let dog = new Dog("Rex", "Labrador");
    dog.speak();
    console.log(`Breed: ${dog.getBreed()}`);

    let cat = new Cat("Whiskers");
    cat.speak();
    cat.play();
})();
