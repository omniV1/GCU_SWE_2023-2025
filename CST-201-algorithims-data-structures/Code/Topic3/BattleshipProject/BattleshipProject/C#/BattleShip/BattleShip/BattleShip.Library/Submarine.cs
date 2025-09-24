
namespace BattleShip.Library
{
    public class Submarine : Ship
    {
        public const int SubmarineSize = 3;

        public bool Upwards { get; set; }
        public bool Left { get; set; }

        public Submarine(string name, char symbol) :
            base(name, Ship.ShipTypes.Submarine, symbol)
        {
            Upwards = false;
            Left = false;
        }
    }
}
