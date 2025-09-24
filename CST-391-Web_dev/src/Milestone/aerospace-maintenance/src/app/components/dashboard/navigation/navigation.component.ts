/**
 * Navigation component providing the main navigation structure
 * Includes a responsive sidebar and toolbar with routing capabilities
 */
import { Component } from '@angular/core';
import { Router } from '@angular/router';

@Component({
  selector: 'app-navigation',
  standalone: false, 
  templateUrl: './navigation.component.html',
  styleUrls: ['./navigation.component.scss']
})
export class NavigationComponent {
  // Navigation links configuration
  // Each link defines path, icon, label, and exact matching requirement
  links = [
    { path: '/dashboard', icon: 'dashboard', label: 'Dashboard', exact: true },
    { path: '/aircraft', icon: 'flight', label: 'Aircraft Fleet', exact: true }
    // Maintenance and performance accessed through aircraft views
  ];

  constructor(private router: Router) {}

  /**
   * Determines if a route is currently active
   * @param path - Route path to check
   * @param exact - Whether to match the route exactly
   * @returns boolean indicating if route is active
   */
  isActive(path: string, exact: boolean): boolean {
    return this.router.isActive(path, exact);
  }
}