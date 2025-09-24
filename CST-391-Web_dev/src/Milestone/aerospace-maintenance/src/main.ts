/**
 * Main entry point for the Angular application.
 * 
 * This file imports the necessary modules and bootstraps the Angular application
 * using the `platformBrowserDynamic` function. It attempts to bootstrap the `AppModule`
 * and logs any errors to the console if the bootstrap process fails.
 * 
 * @module Main
 */
import { platformBrowserDynamic } from '@angular/platform-browser-dynamic';
import { AppModule } from './app/app.module';

platformBrowserDynamic().bootstrapModule(AppModule)
  .catch(err => console.error(err));