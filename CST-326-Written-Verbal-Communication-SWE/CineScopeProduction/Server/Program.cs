using CineScope.Server.Interfaces;
using CineScope.Server.Services;
using CineScope.Server.Data;
using Microsoft.AspNetCore.Builder;
using Microsoft.Extensions.Hosting;
using Microsoft.Extensions.DependencyInjection;
using Microsoft.Extensions.Configuration;
using Microsoft.AspNetCore.Authentication.JwtBearer;
using Microsoft.IdentityModel.Tokens;
using System.Text;
using CineScope.Shared.Config;
using Azure.Identity;

var builder = WebApplication.CreateBuilder(args);



// Configure MVC and Razor Pages
builder.Services.AddControllersWithViews();
builder.Services.AddRazorPages();

// Configure MongoDB settings
builder.Services.Configure<MongoDbSettings>(
    builder.Configuration.GetSection(nameof(MongoDbSettings)));

// Add memory cache
builder.Services.AddMemoryCache();

// Register MongoDB service
builder.Services.AddSingleton<IMongoDbService, MongoDbService>();

// Register caching services
builder.Services.AddSingleton<MovieCacheService>();

// Register other services
builder.Services.AddScoped<AdminService>();
if (builder.Environment.IsDevelopment())
{
    builder.Services.AddScoped<DataSeedService>();
}
builder.Services.AddScoped<IMovieService, MovieService>();
builder.Services.AddScoped<IAuthService, AuthService>();
builder.Services.AddScoped<ReviewService>();
builder.Services.AddScoped<ContentFilterService>();
builder.Services.AddScoped<UserService>();
builder.Services.AddHttpClient<RecaptchaService>();
builder.Services.AddScoped<RecaptchaService>();
builder.Services.AddOptions<RecaptchaSettings>()
    .Bind(builder.Configuration.GetSection("Recaptcha"))
    .Validate(
        settings => !settings.Enabled ||
                    (!string.IsNullOrWhiteSpace(settings.SiteKey) &&
                     !string.IsNullOrWhiteSpace(settings.SecretKey)),
        "Recaptcha__SiteKey and Recaptcha__SecretKey are required when reCAPTCHA is enabled.")
    .ValidateOnStart();

var jwtIssuer = builder.Configuration["JwtSettings:Issuer"]
    ?? throw new InvalidOperationException("JwtSettings__Issuer is required.");
var jwtAudience = builder.Configuration["JwtSettings:Audience"]
    ?? throw new InvalidOperationException("JwtSettings__Audience is required.");
var jwtSecret = builder.Configuration["JwtSettings:Secret"]
    ?? throw new InvalidOperationException("JwtSettings__Secret is required.");

if (Encoding.UTF8.GetByteCount(jwtSecret) < 32)
{
    throw new InvalidOperationException("JwtSettings__Secret must be at least 32 bytes.");
}

builder.Services.AddAuthentication(options =>
{
    options.DefaultAuthenticateScheme = JwtBearerDefaults.AuthenticationScheme;
    options.DefaultChallengeScheme = JwtBearerDefaults.AuthenticationScheme;
})
.AddJwtBearer(options =>
{
    options.TokenValidationParameters = new TokenValidationParameters
    {
        ValidateIssuer = true,
        ValidateAudience = true,
        ValidateLifetime = true,
        ValidateIssuerSigningKey = true,
        ValidIssuer = jwtIssuer,
        ValidAudience = jwtAudience,
        IssuerSigningKey = new SymmetricSecurityKey(Encoding.UTF8.GetBytes(jwtSecret))
    };
});

// Add authorization
builder.Services.AddAuthorization();

builder.Services.AddCors(options =>
{
    options.AddPolicy("AllowAll", policy =>
    {
        policy.AllowAnyOrigin()
              .AllowAnyMethod()
              .AllowAnyHeader();
    });
});

// Now build the app AFTER all service registrations
var app = builder.Build();

// Configure the HTTP request pipeline
if (app.Environment.IsDevelopment())
{
    app.UseDeveloperExceptionPage();
}
else
{
    app.UseExceptionHandler("/Error");
    app.UseHsts();
}

app.UseHttpsRedirection();
app.UseBlazorFrameworkFiles();
app.UseStaticFiles();
app.UseRouting();
app.UseCors("AllowAll");
app.UseAuthentication();
app.UseAuthorization();
app.MapControllers();
app.MapRazorPages();
app.MapFallbackToFile("index.html");

app.Run();
