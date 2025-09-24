// Owen Lindsey
// Only methods PlaceSubmarine, PlaceCruiser, PlaceDestroyer, and PlaceShip are modified by me. 
// The rest of the code is from the instructor of CST-201
// Professor Demland, David
// CST-201
// 10/19/2024
using BattleShip.Library;

var game = new BattleshipGame();

Console.WriteLine("Welcome to Battleship! Let's set up your ships.");
SetPlayerShips(game);

Console.Clear();
Console.WriteLine("Player's board:");
DisplayBoard(game.PlayerBoard);

Console.WriteLine("Computer's board:");
DisplayBoard(game.ComputerBoard);

Console.Clear();
Console.WriteLine("Both boards are set up. Let's start the currGame!");

while (true)
{
    PlayerTurn();
    DisplayBoard(game.PlayerBoard);
    if (game.CheckGameOver(false))
    {
        Console.WriteLine("Congratulations! You've sunk all the computer's ships. You win!");
        break;
    }

    ComputerTurn();
    DisplayBoard(game.PlayerBoard);
    if (!game.CheckGameOver(true))
    {
        continue;
    }

    Console.WriteLine("Game over! The computer has sunk all your ships. You lose.");
    break;
}

Console.WriteLine("Press any key to exit...");
Console.ReadKey();

return;

void DisplayBoard(char[,] board)
{
    Console.WriteLine("   1 2 3 4 5 6 7 8 9 10");
    for (var row = 0; row < BattleshipGame.BoardSize; row++)
    {
        Console.Write($"{row + 1,2} ");
        for (var column = 0; column < BattleshipGame.BoardSize; column++)
        {
            Console.Write(board[row, column] + " ");
        }
        Console.WriteLine();
    }
}

void SetPlayerShips(BattleshipGame currGame)
{
    var playerShips = currGame.PlayerShips;
    for (var shipIdx = 0; shipIdx < 3; shipIdx++)
    {
        var ship = playerShips[shipIdx];
        Console.WriteLine($"Set your {ship.Name} (ship: {ship.Type})");

        while (true)
        {
            Console.Write("Enter the starting position: ");
            var (row, column) = GetUserInput();
            GetPlacementDirections(ship);

            if (!currGame.PlaceShip(currGame.PlayerBoard, row, column, ship))
            {
                Console.WriteLine("Invalid ship placement. Please choose another position.");
                continue;
            }

            break;
        }

        Console.Clear();
        Console.WriteLine("Player's board:");
        DisplayBoard(game.PlayerBoard);
    }
}

(int row, int column) GetUserInput()
{
    var row = GetInput("row");
    var column = GetInput("column");
    return (row - 1, column - 1);
}

int GetInput(string rowOrColumnStr)
{
    while (true)
    {
        Console.Write($"Please enter {rowOrColumnStr}: ");
        var input = Console.ReadLine()?.Trim();
        var num = Convert.ToInt32(input);
        if (GoodInput(num))
        {
            return num;
        }

        Console.Write("Please enter a value of 1 to 10.");
    }
}

bool GoodInput(int num)
{
    return num is >= 1 and <= BattleshipGame.BoardSize;
}

void GetPlacementDirections(Ship ship)
{
    switch (ship.Type)
    {
        case Ship.ShipTypes.Submarine:
            var submarine = (Submarine) ship;
            submarine.Left = GetYesOrNoAnswer("Do you want the Submarine direction to the left (y/n)? ");
            submarine.Upwards = GetYesOrNoAnswer("Do you want the Submarine direction upwards (y/n)? ");
            return;

        case Ship.ShipTypes.Cruiser:
            var cruiser = (Cruiser)ship;
            cruiser.Vertical = GetYesOrNoAnswer("Do you want the Cruiser direction vertical (y/n)? ");
            cruiser.Upwards = GetYesOrNoAnswer("Do you want the Cruiser direction upwards (y/n)? ");
            cruiser.Left = GetYesOrNoAnswer("Do you want the Destroyer direction to the left (y/n)? ");
            return;

        case Ship.ShipTypes.Destroyer:
            var destroyer = (Destroyer)ship;
            destroyer.Left = GetYesOrNoAnswer("Do you want the Destroyer direction to the left (y/n)? ");
            destroyer.Upwards = GetYesOrNoAnswer("Do you want the Destroyer direction upwards (y/n)? ");
            return;

        default:
            return;
    }
}

bool GetYesOrNoAnswer(string prompt)
{
    while (true)
    {
        Console.Write(prompt);
        var answer = Console.ReadLine()?.Trim().ToLower();
        switch (answer)
        {
            case "y":
                return true;

            case "n":
                return false;

            default:
                Console.WriteLine("Please enter y or n.");
                continue;
        }
    }
}

void PlayerTurn()
{
    Console.WriteLine("Your turn!");
    while (true)
    {
        Console.Write("Enter your target position: ");
        var (row, column) = GetUserInput();
        if (game.AlreadyFired(false, row, column))
        {
            Console.WriteLine("You've already fired at this position. Choose another one.");
            continue;
        }

        Console.WriteLine(game.IsHit(false, row, column) ? "Hit!" : "Miss!");

        break;
    }
}

void ComputerTurn()
{
    var random = new Random();
    Console.WriteLine("Computer's turn!");
    Thread.Sleep(1000); // Delay for dramatic effect

    while (true)
    {
        var row = random.Next(BattleshipGame.BoardSize);
        var column = random.Next(BattleshipGame.BoardSize);

        if (game.AlreadyFired(true, row, column))
        {
            continue;
        }

        Console.WriteLine(game.AlreadyFired(true, row, column)
            ? $"Computer hit at {row + 1},{column + 1}!"
            : $"Computer missed at {row + 1},{column + 1}.");

        break;
    }
}
