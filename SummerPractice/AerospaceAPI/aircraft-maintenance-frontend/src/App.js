import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import AircraftList from './components/AircraftList';
import AircraftDetails from './components/AircraftDetails';
import AircraftForm from './components/AircraftForm';
import AircraftEdit from './components/AircraftEdit';
import NavBar from './components/NavBar';
import MaintenanceRecords from './components/MaintenanceRecords';
import './styles/App.css';


function App() {
    return (
        <Router>
            <div className="App">
                <NavBar />
                <Routes>
                    <Route exact path="/" element={<AircraftList />} />
                    <Route path="/add-aircraft" element={<AircraftForm />} />
                    <Route path="/aircrafts/:id" element={<AircraftDetails />} />
                    <Route path="/aircrafts/edit/:id" element={<AircraftEdit />} />
                    <Route path="/aircrafts/:id/maintenance" element={<MaintenanceRecords />} />
                </Routes>
            </div>
        </Router>
    );
}

export default App;
