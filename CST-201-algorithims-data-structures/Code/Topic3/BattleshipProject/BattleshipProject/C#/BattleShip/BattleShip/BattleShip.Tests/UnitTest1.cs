using BattleShip.Library;

namespace BattleShip.Tests
{
    public class Tests
    {
        [Test]
        public void TestInit()
        {
            var game = new BattleshipGame(false);
            var ships = game.PlayerShips;
            Assert.Multiple(() =>
            {
                Assert.That(ships[0].Name, Is.EqualTo("USS Destroyer"));
                Assert.That(ships[0].Type, Is.EqualTo(Ship.ShipTypes.Destroyer));
                Assert.That(ships[0].Symbol, Is.EqualTo('D'));
                Assert.That(ships[1].Name, Is.EqualTo("USS Submarine"));
                Assert.That(ships[1].Type, Is.EqualTo(Ship.ShipTypes.Submarine));
                Assert.That(ships[1].Symbol, Is.EqualTo('S'));
                Assert.That(ships[2].Name, Is.EqualTo("USS Cruiser"));
                Assert.That(ships[2].Type, Is.EqualTo(Ship.ShipTypes.Cruiser));
                Assert.That(ships[2].Symbol, Is.EqualTo('C'));
            });

            ships = game.ComputerShips;
            Assert.Multiple(() =>
            {
                Assert.That(ships[0].Name, Is.EqualTo("NCC Destroyer"));
                Assert.That(ships[0].Type, Is.EqualTo(Ship.ShipTypes.Destroyer));
                Assert.That(ships[0].Symbol, Is.EqualTo('D'));
                Assert.That(ships[1].Name, Is.EqualTo("NCC Submarine"));
                Assert.That(ships[1].Type, Is.EqualTo(Ship.ShipTypes.Submarine));
                Assert.That(ships[1].Symbol, Is.EqualTo('S'));
                Assert.That(ships[2].Name, Is.EqualTo("NCC Cruiser"));
                Assert.That(ships[2].Type, Is.EqualTo(Ship.ShipTypes.Cruiser));
                Assert.That(ships[2].Symbol, Is.EqualTo('C'));
            });

            var playerBoard = game.PlayerBoard;
            var computerBoard = game.ComputerBoard;
            for (var row = 0; row < BattleshipGame.BoardSize; row++)
            {
                for (var column = 0; column < BattleshipGame.BoardSize; column++)
                {
                    Assert.Multiple(() =>
                    {
                        Assert.That(playerBoard[row, column], Is.EqualTo(BattleshipGame.OpenCellChar));
                        Assert.That(computerBoard[row, column], Is.EqualTo(BattleshipGame.OpenCellChar));
                    });
                }
            }
        }

        [Test]
        public void TestCruiserPlacement()
        {
            var game = new BattleshipGame(false);
            var ships = game.PlayerShips;
            var cruiser = (Cruiser)ships[2];
            var placed = game.PlaceCruiser(game.PlayerBoard, 3, 3, cruiser);
            Assert.Multiple(() =>
            {
                Assert.That(placed, Is.True);
                Assert.That('O', Is.EqualTo(game.PlayerBoard[3, 3]));
                Assert.That('O', Is.EqualTo(game.PlayerBoard[3, 4]));
                Assert.That('O', Is.EqualTo(game.PlayerBoard[3, 5]));
            });

            cruiser.Left = true;
            placed = game.PlaceCruiser(game.PlayerBoard, 4, 3, cruiser);
            Assert.Multiple(() =>
            {
                Assert.That(placed, Is.True);
                Assert.That('O', Is.EqualTo(game.PlayerBoard[4, 3]));
                Assert.That('O', Is.EqualTo(game.PlayerBoard[4, 2]));
                Assert.That('O', Is.EqualTo(game.PlayerBoard[4, 1]));
            });

            cruiser.Left = false;
            cruiser.Vertical = true;
            placed = game.PlaceCruiser(game.PlayerBoard, 7, 3, cruiser);
            Assert.Multiple(() =>
            {
                Assert.That(placed, Is.True);
                Assert.That('O', Is.EqualTo(game.PlayerBoard[7, 3]));
                Assert.That('O', Is.EqualTo(game.PlayerBoard[8, 3]));
                Assert.That('O', Is.EqualTo(game.PlayerBoard[9, 3]));
            });

            cruiser.Upwards = true;
            placed = game.PlaceCruiser(game.PlayerBoard, 7, 4, cruiser);
            Assert.Multiple(() =>
            {
                Assert.That(placed, Is.True);
                Assert.That('O', Is.EqualTo(game.PlayerBoard[7, 4]));
                Assert.That('O', Is.EqualTo(game.PlayerBoard[6, 4]));
                Assert.That('O', Is.EqualTo(game.PlayerBoard[5, 4]));
            });

            //
            //  Bad Placements
            //

            cruiser.Upwards = false;
            cruiser.Vertical = false;
            cruiser.Left = false;
            placed = game.PlaceCruiser(game.PlayerBoard, 9, 9, cruiser);
            Assert.That(placed, Is.False);

            cruiser.Left = true;
            placed = game.PlaceCruiser(game.PlayerBoard, 1, 1, cruiser);
            Assert.That(placed, Is.False);

            cruiser.Left = false;
            cruiser.Vertical = true;
            placed = game.PlaceCruiser(game.PlayerBoard, 9, 3, cruiser);
            Assert.That(placed, Is.False);

            cruiser.Upwards = false;
            placed = game.PlaceCruiser(game.PlayerBoard, 9, 1, cruiser);
            Assert.That(placed, Is.False);
        }

        [Test]
        public void TestDestroyerPlacement()
        {
            var game = new BattleshipGame(false);
            var ships = game.PlayerShips;
            var destroyer = (Destroyer)ships[0];
            var placed = game.PlaceDestroyer(game.PlayerBoard, 3, 3, destroyer);
            Assert.Multiple(() =>
            {
                Assert.That(placed, Is.True);
                Assert.That('O', Is.EqualTo(game.PlayerBoard[3, 3]));
                Assert.That('O', Is.EqualTo(game.PlayerBoard[3, 4]));
                Assert.That('O', Is.EqualTo(game.PlayerBoard[4, 3]));
                Assert.That('O', Is.EqualTo(game.PlayerBoard[4, 4]));
            });

            destroyer.Left = true;
            placed = game.PlaceDestroyer(game.PlayerBoard, 2, 7, destroyer);
            Assert.Multiple(() =>
            {
                Assert.That(placed, Is.True);
                Assert.That('O', Is.EqualTo(game.PlayerBoard[2, 7]));
                Assert.That('O', Is.EqualTo(game.PlayerBoard[2, 6]));
                Assert.That('O', Is.EqualTo(game.PlayerBoard[3, 7]));
                Assert.That('O', Is.EqualTo(game.PlayerBoard[3, 6]));
            });

            destroyer.Left = false;
            destroyer.Upwards = true;
            placed = game.PlaceDestroyer(game.PlayerBoard, 7, 3, destroyer);
            Assert.Multiple(() =>
            {
                Assert.That(placed, Is.True);
                Assert.That('O', Is.EqualTo(game.PlayerBoard[6, 3]));
                Assert.That('O', Is.EqualTo(game.PlayerBoard[6, 4]));
                Assert.That('O', Is.EqualTo(game.PlayerBoard[7, 3]));
                Assert.That('O', Is.EqualTo(game.PlayerBoard[7, 4]));
            });

            destroyer.Left = true;
            placed = game.PlaceDestroyer(game.PlayerBoard, 7, 6, destroyer);
            Assert.Multiple(() =>
            {
                Assert.That(placed, Is.True);
                Assert.That('O', Is.EqualTo(game.PlayerBoard[7, 5]));
                Assert.That('O', Is.EqualTo(game.PlayerBoard[7, 6]));
                Assert.That('O', Is.EqualTo(game.PlayerBoard[6, 5]));
                Assert.That('O', Is.EqualTo(game.PlayerBoard[6, 6]));
            });

            //
            //  Bad Placements
            //

            destroyer.Upwards = false;
            destroyer.Left = false;
            placed = game.PlaceDestroyer(game.PlayerBoard, 10, 10, destroyer);
            Assert.That(placed, Is.False);

            destroyer.Left = true;
            placed = game.PlaceDestroyer(game.PlayerBoard, 10, 1, destroyer);
            Assert.That(placed, Is.False);

            destroyer.Left = false;
            destroyer.Upwards = true;
            placed = game.PlaceDestroyer(game.PlayerBoard, 1, 10, destroyer);
            Assert.That(placed, Is.False);

            destroyer.Left = true;
            placed = game.PlaceDestroyer(game.PlayerBoard, 0, 0, destroyer);
            Assert.That(placed, Is.False);
        }

        [Test]
        public void TestSubmarinePlacement()
        {
            var game = new BattleshipGame(false);
            var ships = game.PlayerShips;
            var submarine = (Submarine)ships[1];
            var placed = game.PlaceSubmarine(game.PlayerBoard, 4, 4, submarine);
            Assert.Multiple(() =>
            {
                Assert.That(placed, Is.True);
                Assert.That('O', Is.EqualTo(game.PlayerBoard[4, 4]));
                Assert.That('O', Is.EqualTo(game.PlayerBoard[5, 5]));
                Assert.That('O', Is.EqualTo(game.PlayerBoard[6, 6]));
            });

            submarine.Left = true;
            placed = game.PlaceSubmarine(game.PlayerBoard, 4, 3, submarine);
            Assert.Multiple(() =>
            {
                Assert.That(placed, Is.True);
                Assert.That('O', Is.EqualTo(game.PlayerBoard[4, 3]));
                Assert.That('O', Is.EqualTo(game.PlayerBoard[5, 2]));
                Assert.That('O', Is.EqualTo(game.PlayerBoard[6, 1]));
            });

            submarine.Left = false;
            submarine.Upwards = true;
            placed = game.PlaceSubmarine(game.PlayerBoard, 3, 4, submarine);
            Assert.Multiple(() =>
            {
                Assert.That(placed, Is.True);
                Assert.That('O', Is.EqualTo(game.PlayerBoard[3, 4]));
                Assert.That('O', Is.EqualTo(game.PlayerBoard[2, 5]));
                Assert.That('O', Is.EqualTo(game.PlayerBoard[1, 6]));
            });

            submarine.Left = true;
            placed = game.PlaceSubmarine(game.PlayerBoard, 3, 3, submarine);
            Assert.Multiple(() =>
            {
                Assert.That(placed, Is.True);
                Assert.That('O', Is.EqualTo(game.PlayerBoard[3, 3]));
                Assert.That('O', Is.EqualTo(game.PlayerBoard[2, 2]));
                Assert.That('O', Is.EqualTo(game.PlayerBoard[1, 1]));
            });

            //
            //  Bad Placements
            //

            submarine.Upwards = false;
            submarine.Left = false;
            placed = game.PlaceSubmarine(game.PlayerBoard, 10, 10, submarine);
            Assert.That(placed, Is.False);

            submarine.Left = true;
            placed = game.PlaceSubmarine(game.PlayerBoard, 10, 1, submarine);
            Assert.That(placed, Is.False);

            submarine.Left = false;
            submarine.Upwards = true;
            placed = game.PlaceSubmarine(game.PlayerBoard, 1, 10, submarine);
            Assert.That(placed, Is.False);

            submarine.Left = true;
            placed = game.PlaceSubmarine(game.PlayerBoard, 0, 0, submarine);
            Assert.That(placed, Is.False);
        }

        [Test]
        public void TestEndGame()
        {
            var game = new BattleshipGame(false);
            var playerEndGame = game.CheckGameOver(true);
            var computerEndGame = game.CheckGameOver(false);
            Assert.Multiple(() =>
            {
                Assert.That(playerEndGame, Is.True);
                Assert.That(computerEndGame, Is.True);
            });

            game = null;
            game = new BattleshipGame(true);
            game.PlaceCruiser(game.PlayerBoard, 5, 5, new Cruiser("Cruiser 1", 'C'));
            playerEndGame = game.CheckGameOver(true);
            computerEndGame = game.CheckGameOver(false);
            Assert.Multiple(() =>
            {
                Assert.That(playerEndGame, Is.False);
                Assert.That(computerEndGame, Is.False);
            });
        }
    }
}
