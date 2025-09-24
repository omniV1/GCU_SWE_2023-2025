namespace BattleShip.Library
{
    public class Ship
    {
        public enum ShipTypes
        {
            Destroyer,
            Submarine,
            Cruiser
        }

        public string Name { get; }
        public ShipTypes Type { get; }
        public char Symbol { get; }

        public Ship(string name, ShipTypes type, char symbol)
        {
            Name = name;
            Type = type;
            Symbol = symbol;
        }
    }
}
