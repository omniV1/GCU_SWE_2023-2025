using Milestone.Models.GameModels;
using System;

namespace Milestone.Services.Business.Interfaces
{
    public interface IGameService
    {
        Board CreateGame(string difficulty);
        CellUpdateResponse RevealCell(int row, int col, Guid gameId);
        Board GetGame(Guid gameId);
    }
}
