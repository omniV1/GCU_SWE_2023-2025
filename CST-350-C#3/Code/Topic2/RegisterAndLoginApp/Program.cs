var builder = WebApplication.CreateBuilder(args);

// Add services to the container.
builder.Services.AddControllersWithViews();

// Add our session services 
builder.Services.AddDistributedMemoryCache();

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