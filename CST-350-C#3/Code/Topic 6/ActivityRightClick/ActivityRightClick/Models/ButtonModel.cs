namespace ActivityRightClick.Models
{
    public class ButtonModel
    {
        // Model Properties
        public int Id { get; set; }
        public int ButtonState { get; set; }

        /// <summary>
        /// Default constructor
        /// </summary>
        public ButtonModel()
        {
            // empty 
        }

        /// <summary>
        /// Parameterized constructor
        /// </summary>
        /// <param name="id"></param>
        /// <param name="buttonState"></param>
        public ButtonModel(int id, int buttonState)
        {
            Id = id;
            ButtonState = buttonState;
        }

    }
}
