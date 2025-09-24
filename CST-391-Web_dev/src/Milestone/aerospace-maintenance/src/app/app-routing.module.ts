import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { DashboardComponent } from './components/dashboard/dashboard.component';
import { AircraftListComponent } from './components/aircraft-list/aircraft-list.component';
import { MaintenanceHistoryComponent } from './components/maintenance-history/maintenance-history.component';
import { PerformanceMetricsComponent } from './components/performance-metrics/performance-metrics.component';
import { PerformanceAnalyticsComponent } from './components/performance-analytics/performance-analytics.component';

const routes: Routes = [
  // Redirect root to dashboard
  { path: '', redirectTo: '/dashboard', pathMatch: 'full' },
  
  // Dashboard route
  { path: 'dashboard', component: DashboardComponent },
  
  // Aircraft routes
  { path: 'aircraft', component: AircraftListComponent },
  
  // Nested routes for specific aircraft
  { path: 'aircraft/:id', children: [
    { path: 'maintenance', component: MaintenanceHistoryComponent },
    { path: 'performance', component: PerformanceMetricsComponent },
    { path: 'performance/analytics', component: PerformanceAnalyticsComponent }
  ]},

  // Catch all route - redirect to dashboard
  { path: '**', redirectTo: '/dashboard' }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }