(function () {
    function greet(name, greeting) {
        if (greeting === void 0) { greeting = "Hello"; }
        return "".concat(greeting, ", ").concat(name, "!");
    }
    console.log(greet("Alice"));
    console.log(greet("Bob", "Hi"));
    var multiply = function (a, b) {
        if (b === void 0) { b = 1; }
        return a * b;
    };
    console.log(multiply(5, 2));
    console.log(multiply(5));
})();
