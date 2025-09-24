using MinesweeperGui.PresentationLayer;

namespace MinesweeperGui
{
    internal static class Program
    {
        /// <summary>
        ///  The main entry point for the application.
        /// </summary>
        [STAThread]
        static void Main()
        {
            Application.EnableVisualStyles();
            Application.SetCompatibleTextRenderingDefault(false);
            FrmDifficulty FrmDifficulty = new();

            if (FrmDifficulty.ShowDialog() == DialogResult.OK)
            {
                string difficulty = FrmDifficulty.SelectedDifficulty;
                Application.Run(new FrmMain(difficulty));
            }
        }
    }
}
    