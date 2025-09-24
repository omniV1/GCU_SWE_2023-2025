
namespace BattleShip.Library
{
    public class Cruiser : Ship
    {
        public const int CruiserSize = 3;

        public bool Vertical { get; set; }
        public bool Upwards { get; set; }
        public bool Left { get; set; }

        public Cruiser(string name, char symbol) :
                    base(name, Ship.ShipTypes.Cruiser, symbol)
        {
            Vertical = false;
            Left = false;
            Upwards = false;
        }
    }
}
