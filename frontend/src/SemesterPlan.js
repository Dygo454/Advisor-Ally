import React, { useState } from 'react';
import { Link, useNavigate } from 'react-router-dom';

function SemesterPlan() {
    const navigate = useNavigate();

    const requestOptions = {
        method: 'GET'
    };
    fetch("http://localhost:5000/whatif",requestOptions).then((resp) => {
        if (resp.status === 401) {
            alert("Not signed in!")
            navigate("/login")
        }
        else if (resp.status === 200) {
            resp.json().then((json) => {
                const requestOptions2 = {
                    method: 'POST',
                    headers: {'Content-Type': 'application/json'},
                    body: JSON.stringify(json)
                };
                fetch("http://localhost:5000/get_schedule",requestOptions2).then((resp) => {
                    console.log(resp);
                    if (resp.status === 401) {
                        alert("Not signed in!")
                        navigate("/login")
                    }
                    else if (resp.status === 200) {
                        resp.json().then((json) => {
                            document.getElementById("plan").innerText = json.data;
                        });
                    }
                    else {
                        ;
                    }
                });
            });
        }
        else {
            ;
        }
    });
    return (
        <p id="plan"></p>
    );
}

export default SemesterPlan;