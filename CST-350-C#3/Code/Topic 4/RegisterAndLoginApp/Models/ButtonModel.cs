namespace RegisterAndLoginApp.Models
{
    public class ButtonModel
    {
        public int Id { get; set; }
        public int ButtonState { get; set; }

        // Removing button image temporarily 
        // public string ButtonImage { get; set; }

        public ButtonModel()
        {

        }

        public ButtonModel(int id, int buttonState)
        {
            Id = id;
            ButtonState = buttonState;
            
        }
    }
}
