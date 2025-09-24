import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable, forkJoin, throwError } from 'rxjs';
import { map, catchError } from 'rxjs/operators';
import { Aircraft, AircraftWithMaintenance, AircraftStatus } from '../models/aircraft.model';
import {  MaintenanceStatus } from '../models/maintenance.model';
import { OperatorFunction } from 'rxjs';
import { MaintenanceRecord } from '../models/maintenance.model';
import { PerformanceMetric, NewPerformanceMetric } from '../models/performance.model';

@Injectable({
  providedIn: 'root'
})
export class AircraftService {
  private apiUrl = 'http://localhost:5000/api';
  private maintenanceApiUrl = 'http://localhost:5000/api/maintenancerecord';

  constructor(private http: HttpClient) { }

getAllAircraft(): Observable<AircraftWithMaintenance[]> {
  return forkJoin({
    aircraft: this.http.get<Aircraft[]>(`${this.apiUrl}/aircraft`),
    maintenance: this.http.get<MaintenanceRecord[]>(`${this.apiUrl}/maintenance`)
  }).pipe(
    map(({ aircraft, maintenance }) => {
      return aircraft.map(aircraft => {
        const aircraftMaintenance = maintenance
          .filter(record => record.AircraftID === aircraft.aircraftID)
          .sort((a, b) => new Date(b.MaintenanceDate).getTime() - new Date(a.MaintenanceDate).getTime());

        const latestMaintenance = aircraftMaintenance[0];

        return {
          ...aircraft,
          lastMaintenanceDate: latestMaintenance ? new Date(latestMaintenance.MaintenanceDate) : undefined,
          nextMaintenanceDate: latestMaintenance?.nextDueDate ? new Date(latestMaintenance.nextDueDate) : undefined,
          aircraftID: aircraft.aircraftID,
          engineHours: aircraft.engineHours,
          maintenanceStatus: this.calculateMaintenanceStatus(latestMaintenance?.nextDueDate)
        };
      });
    })
  );
}

createAircraft(aircraft: Aircraft): Observable<AircraftWithMaintenance> {
  return this.http.post<AircraftWithMaintenance>(`${this.apiUrl}/aircraft`, aircraft);
}

updateAircraft(aircraft: Aircraft): Observable<AircraftWithMaintenance> {
  return this.http.put<AircraftWithMaintenance>(`${this.apiUrl}/aircraft/${aircraft.aircraftID}`, aircraft);
}

deleteAircraft(aircraftId: number): Observable<void> {
  return this.http.delete<void>(`${this.apiUrl}/aircraft/${aircraftId}`);
}

getMaintenanceHistory(aircraftId: number): Observable<MaintenanceRecord[]> {
  console.log(`Getting maintenance history for aircraft ${aircraftId}`);
  return this.http.get<MaintenanceRecord[]>(
    `${this.apiUrl}/maintenancerecord/aircraft/${aircraftId}`
  );
}

  private calculateMaintenanceStatus(nextDueDate?: Date): MaintenanceStatus {
    if (!nextDueDate) return MaintenanceStatus.SCHEDULED;
  
    const today = new Date();
    const daysUntilMaintenance = Math.ceil(
      (new Date(nextDueDate).getTime() - today.getTime()) / (1000 * 3600 * 24)
    );
  
    // Update these return values to match your enum
    if (daysUntilMaintenance < 0) return MaintenanceStatus.DEFERRED;
    if (daysUntilMaintenance <= 3) return MaintenanceStatus.IN_PROGRESS;
    return MaintenanceStatus.SCHEDULED;
  }

  private getAircraftStatus(status: string): AircraftStatus {
    switch(status.toLowerCase()) {
      case 'ready':
        return AircraftStatus.READY;
      case 'not ready':
        return AircraftStatus.NOT_READY;
      case 'in maintenance':
        return AircraftStatus.IN_MAINTENANCE;
      default:
        return AircraftStatus.NOT_READY;
    }
  }

  addMaintenanceRecord(aircraftId: number, record: MaintenanceRecord): Observable<MaintenanceRecord> {
    return this.http.post<MaintenanceRecord>(`${this.maintenanceApiUrl}/aircraft/${aircraftId}`, record);
  }

  updateMaintenanceRecord(aircraftId: number, record: MaintenanceRecord): Observable<MaintenanceRecord> {
    console.log('Service updating record:', record); // Debug log
    console.log(`URL: ${this.maintenanceApiUrl}/aircraft/${aircraftId}/${record.MaintenanceID}`); // Log the URL
    return this.http.put<MaintenanceRecord>(
      `${this.maintenanceApiUrl}/aircraft/${aircraftId}/${record.MaintenanceID}`, 
      record
    ).pipe(
      tap(response => console.log('Server response:', response)), // Log the response
      catchError(error => {
        console.error('Service error:', error);
        return throwError(() => error);
      })
    );
  }

  deleteMaintenanceRecord(aircraftId: number, recordId: number): Observable<void> {
    return this.http.delete<void>(`${this.maintenanceApiUrl}/aircraft/${aircraftId}/${recordId}`);
  }

 

  addPerformanceRecord(aircraftId: number, record: NewPerformanceMetric): Observable<PerformanceMetric> {
    const recordToSend = {
      ...record,
      AircraftID: aircraftId,
      FuelConsumption: record.FuelConsumption  // Make sure field name matches
    };
    
    console.log('Sending record:', recordToSend); // Add logging
    
    return this.http.post<PerformanceMetric>(
      `${this.apiUrl}/performance`, 
      recordToSend
    ).pipe(
      catchError(error => {
        console.error('Error adding performance record:', error);
        return throwError(() => error);
      })
    );
  }
    

  
getPerformanceRecordsByAircraftId(aircraftId: number): Observable<PerformanceMetric[]> {
  return this.http.get<PerformanceMetric[]>(`${this.apiUrl}/performance/aircraft/${aircraftId}`);
}


updatePerformanceRecord(aircraftId: number, record: PerformanceMetric): Observable<PerformanceMetric> {
  return this.http.put<PerformanceMetric>(`${this.apiUrl}/performance/${record.MetricID}`, record);
}

deletePerformanceRecord(aircraftId: number, metricId: number): Observable<void> {
  return this.http.delete<void>(`${this.apiUrl}/performance/${metricId}`);
}
}
function tap<T>(next: (value: T) => void): OperatorFunction<T, T> {
  return (source) => new Observable<T>((observer) => {
    return source.subscribe({
      next(value) {
        try {
          next(value);
        } catch (err) {
          observer.error(err);
          return;
        }
        observer.next(value);
      },
      error(err) {
        observer.error(err);
      },
      complete() {
        observer.complete();
      }
    });
  });

}

