(() => {
    function greet(name: string, greeting: string = "Hello"): string {
        return `${greeting}, ${name}!`;
    }

    console.log(greet("Alice"));
    console.log(greet("Bob", "Hi"));

    let multiply = (a: number, b: number = 1): number => a * b;
    console.log(multiply(5, 2));
    console.log(multiply(5));
})();
