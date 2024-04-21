import './App.css';
import React from 'react';
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import Login from './Login';
import Signup from './Signup';
import Info from './Info';
import SemesterPlan from './SemesterPlan';

import "bootstrap/dist/css/bootstrap.min.css";

function App() {
    return (
        <BrowserRouter>
            <Routes>
                <Route path='' element={<Login />}></Route>
                <Route path='/login' element={<Login />}></Route>
                <Route path='/signup' element={<Signup />}></Route>
                <Route path='/info' element={<Info />}></Route>
                <Route path='/plan' element={<SemesterPlan />}></Route>
            </Routes>
        </BrowserRouter>

    );
}

export default App;
