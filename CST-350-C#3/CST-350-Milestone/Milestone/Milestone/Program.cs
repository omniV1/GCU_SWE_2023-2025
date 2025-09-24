using Milestone.Services.Buisness;
using Milestone.Services.Business;
using Milestone.Services.Business.Interfaces;
using Milestone.Services.Data;
using Milestone.Services.Data.DAO;
using Milestone.Services.Data.Interfaces;



var builder = WebApplication.CreateBuilder(args);

// Add services to the container.
builder.Services.AddControllersWithViews();

// Add our session services 
builder.Services.AddDistributedMemoryCache();

builder.Services.AddControllersWithViews();

builder.Services.AddSingleton<IGameDAO, GameDAO>();      // Changed from AddScoped
builder.Services.AddSingleton<GameBoardManager>();       // Changed from AddScoped
builder.Services.AddScoped<IGameService, GameService>(); // This can stay Scoped
builder.Services.AddScoped<SavedGameDAO>();


builder.Services.AddLogging(logging =>
{
    logging.ClearProviders();
    logging.AddConsole();
    logging.AddDebug();
});
builder.Services.AddControllersWithViews();

builder.Services.AddSession(options =>
{
    // set the session time out
    options.IdleTimeout = TimeSpan.FromMinutes(30);

    // Make the session HTTP only
    options.Cookie.HttpOnly = true;

    // Make the session cookie essential 
    options.Cookie.IsEssential = true;
});

var app = builder.Build();

// Configure the HTTP request pipeline.
if (!app.Environment.IsDevelopment())
{
    app.UseExceptionHandler("/Home/Error");
    app.UseHsts();
}

app.UseHttpsRedirection();
app.UseStaticFiles();

app.UseRouting();

// Added to enable sessions and keep login state
app.UseSession();

app.UseAuthorization();


app.MapControllerRoute(
    name: "default",
    pattern: "{controller=Home}/{action=Index}/{id?}");

app.Run();