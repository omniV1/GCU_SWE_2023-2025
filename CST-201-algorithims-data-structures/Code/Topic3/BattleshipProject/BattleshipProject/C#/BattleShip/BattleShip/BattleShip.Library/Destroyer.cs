
namespace BattleShip.Library
{
    public class Destroyer : Ship
    {
        //
        //  Destroyer is a 2 X 2 square
        //

        public const int DestroyerSize = 2;

        public bool Upwards { get; set; }
        public bool Left { get; set; }

        public Destroyer(string name, char symbol) :
                    base(name, Ship.ShipTypes.Destroyer, symbol)
        {
            Upwards = false;
            Left = false;
        }
    }
}
