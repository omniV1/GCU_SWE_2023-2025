(function () {
    var age = 20;
    if (age > 18) {
        console.log("Adult");
    }
    else if (age > 12) {
        console.log("Teenager");
    }
    else {
        console.log("Child");
    }
    var day = new Date().getDay();
    switch (day) {
        case 0:
            console.log("Sunday");
            break;
        case 1:
            console.log("Monday");
            break;
        case 2:
            console.log("Tuesday");
            break;
        case 3:
            console.log("Wednesday");
            break;
        case 4:
            console.log("Thursday");
            break;
        case 5:
            console.log("Friday");
            break;
        default:
            console.log("Saturday");
    }
})();
