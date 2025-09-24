var __extends = (this && this.__extends) || (function () {
    var extendStatics = function (d, b) {
        extendStatics = Object.setPrototypeOf ||
            ({ __proto__: [] } instanceof Array && function (d, b) { d.__proto__ = b; }) ||
            function (d, b) { for (var p in b) if (Object.prototype.hasOwnProperty.call(b, p)) d[p] = b[p]; };
        return extendStatics(d, b);
    };
    return function (d, b) {
        if (typeof b !== "function" && b !== null)
            throw new TypeError("Class extends value " + String(b) + " is not a constructor or null");
        extendStatics(d, b);
        function __() { this.constructor = d; }
        d.prototype = b === null ? Object.create(b) : (__.prototype = b.prototype, new __());
    };
})();
(function () {
    var Animal = /** @class */ (function () {
        function Animal(name) {
            this.name = name;
        }
        Animal.prototype.getName = function () {
            return this.name;
        };
        Animal.prototype.speak = function () {
            console.log("".concat(this.name, " makes a sound."));
        };
        return Animal;
    }());
    var Dog = /** @class */ (function (_super) {
        __extends(Dog, _super);
        function Dog(name, breed) {
            var _this = _super.call(this, name) || this;
            _this.breed = breed;
            return _this;
        }
        Dog.prototype.getBreed = function () {
            return this.breed;
        };
        Dog.prototype.speak = function () {
            console.log("".concat(this.getName(), " barks."));
        };
        return Dog;
    }(Animal));
    var Cat = /** @class */ (function (_super) {
        __extends(Cat, _super);
        function Cat() {
            return _super !== null && _super.apply(this, arguments) || this;
        }
        Cat.prototype.speak = function () {
            console.log("".concat(this.getName(), " meows."));
        };
        Cat.prototype.play = function () {
            console.log("".concat(this.getName(), " is playing."));
        };
        return Cat;
    }(Animal));
    var dog = new Dog("Rex", "Labrador");
    dog.speak();
    console.log("Breed: ".concat(dog.getBreed()));
    var cat = new Cat("Whiskers");
    cat.speak();
    cat.play();
})();
