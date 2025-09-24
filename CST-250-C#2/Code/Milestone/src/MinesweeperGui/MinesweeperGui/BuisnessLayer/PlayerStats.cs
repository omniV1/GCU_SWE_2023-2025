using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;

namespace MinesweeperGui.BusinessLayer
{
    public class PlayerStats : IComparable<PlayerStats>
    {
        public string PlayerInitials { get; set; }
        public string Difficulty { get; set; }
        public TimeSpan TimeElapsed { get; set; }
        public int Score => CalculateScore();

        // Implement IComparable<PlayerStats> to sort by score
        public int CompareTo(PlayerStats other)
        {
            // Higher score is "less" to sort in descending order
            return other.Score.CompareTo(this.Score);
        }

        // Helper method to serialize a PlayerStats object to a string
        public override string ToString()
        {
            // Serialize to a comma-separated line
            return $"{PlayerInitials},{Difficulty},{TimeElapsed.Ticks}";
        }

        // Helper method to deserialize a string to a PlayerStats object
        public static PlayerStats FromString(string line)
        {
            var parts = line.Split(',');
            return new PlayerStats
            {
                PlayerInitials = parts[0],
                Difficulty = parts[1],
                TimeElapsed = TimeSpan.FromTicks(long.Parse(parts[2]))
            };
        }

        private int CalculateScore()
        {
            // Simplified scoring formula for demonstration
            return (int)(100000 - TimeElapsed.TotalSeconds * DifficultyMultiplier());
        }

        private double DifficultyMultiplier()
        {
            return Difficulty switch
            {
                "Hard" => 1.0,
                "Medium" => 1.5,
                "Easy" => 2.0,
                _ => 2.0,
            };
        }
    }

    public static class HighScoresManager
    {
        public static void SaveHighScores(IEnumerable<PlayerStats> highScores, string filePath)
        {
            var lines = highScores.Select(stats => stats.ToString());
            File.WriteAllLines(filePath, lines);
        }

        public static List<PlayerStats> LoadHighScores(string filePath)
        {
            if (!File.Exists(filePath))
                return new List<PlayerStats>();

            var lines = File.ReadAllLines(filePath);
            return lines.Select(PlayerStats.FromString).ToList();
        }
    }
}
