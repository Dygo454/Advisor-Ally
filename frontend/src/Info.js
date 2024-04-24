import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';

import {
    MDBContainer,
    MDBTextArea
}
    from 'mdb-react-ui-kit';

let loadInterval;
let i = 0;

function Info() {

    const [selectedValue, setSelectedValue] = useState('');

    const handleSelectChange = (event) => {
        setSelectedValue(event.target.value);
    };
    let shib="_shibsession_68747470733a2f2f73702e6c6f67696e2e75666c2e6564752f75726e3a6564753a75666c3a70726f643a30303734312f68747470733a2f2f73702e6c6f67696e2e75666c2e6564752f75726e3a6564753a75666c3a70726f643a30303734312f"

    const navigate = useNavigate();

    const handleContinue = () => {
        if (document.getElementById("button").firstChild.nodeValue != "Continue") {
            return;
        }
        let prompt = document.getElementById("prompt").value;
        const requestOptions = {
            method: 'GET'
        };
        document.getElementById("button").firstChild.nodeValue = "loading";
        loadInterval = setInterval(() => {
            document.getElementById("button").firstChild.nodeValue += ".";
            if (i >= 3) {
                document.getElementById("button").firstChild.nodeValue = "Loading.";
                i = 0;
            }
            i++;
        }, 500);
        fetch("http://localhost:5000/whatif?session="+localStorage.getItem(shib)+"&major="+document.getElementById("my-dropdown").value,requestOptions).then((resp) => {
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
                    fetch("http://localhost:5000/get_schedule?prompt="+prompt,requestOptions2).then((resp) => {
                        if (resp.status === 401) {
                            alert("Not signed in!")
                            navigate("/login")
                        }
                        else if (resp.status === 200) {
                            resp.json().then((json) => {
                                localStorage.setItem("data",json.data);
                                clearInterval(loadInterval);
                                document.getElementById("button").firstChild.nodeValue = "Continue";
                                navigate("/plan");
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
    };

    return (
        <>
            <div style={{ paddingTop: '4rem' }}>
                <h2 className='mb-4 text-center' style={{ fontSize: '24px' }}>Welcome to Advisor Ally!</h2>
                <p className='text-center' style={{ fontSize: '18px' }}>Answer the following questions to have your semester plan created.</p>

                <MDBContainer className='p-3 my-5 d-flex flex-column w-50' style={{ border: '1px solid #ced4da', borderRadius: '0.25rem', boxShadow: '0 0.5rem 1rem regba(0, 0, 0, 0.15' }}>
                    <div>
                        <label htmlFor='my-dropdown' style={{ marginRight: '10px' }}>Select a major</label>
                        <select id='my-dropdown' value={ selectedValue }>
                            <option value='ARO_BSAE'>Aerospace Engineering</option>
                            <option value='BE_BSBE'>Biological Engineering</option>
                            <option value='CPE_BSCO'>Computer Engineering</option>
                            <option value='CPS_BSCS'>Computer Science</option>
                            <option value='ELE_BSEE'>Electrical Engineering</option>
                        </select>   
                        <br/>
                        <br/>
                        <label htmlFor='my-dropdown' style={{ marginRight: '10px' }}>Input extra info:</label>
                        <MDBTextArea id='prompt'></MDBTextArea>
                    </div>
                </MDBContainer>

                <div style={{ display: 'flex', justifyContent: 'center', alignItems: 'center', height: '100vh'}} >
                    <button id="button" className='mt-4 mb-4 custom-button' onClick={ handleContinue }>Continue</button>
                </div>


            </div>
        </>
    );
}

export default Info;