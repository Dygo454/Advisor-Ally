import React from 'react';
import { useNavigate } from 'react-router-dom';
import './style.css';

import {
    MDBContainer,
    MDBBtn,
    MDBTextArea
}
    from 'mdb-react-ui-kit';

let i = 0;
let loadInterval;

function SemesterPlan() {
    let navigate = useNavigate();
    let shib="_shibsession_68747470733a2f2f73702e6c6f67696e2e75666c2e6564752f75726e3a6564753a75666c3a70726f643a30303734312f68747470733a2f2f73702e6c6f67696e2e75666c2e6564752f75726e3a6564753a75666c3a70726f643a30303734312f";
    let generatePlan = () => {
        document.getElementById("planTitle").innerText = "";
        document.getElementById("plan").innerText = "";
        if (document.getElementById("button").firstChild.nodeValue != "Submit") {
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
                document.getElementById("button").firstChild.nodeValue = "loading.";
                i = 0;
            }
            i++;
        }, 500);
        fetch("http://localhost:5000/whatif?session="+localStorage.getItem(shib),requestOptions).then((resp) => {
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
                        console.log(resp);
                        if (resp.status === 401) {
                            alert("Not signed in!")
                            navigate("/login")
                        }
                        else if (resp.status === 200) {
                            resp.json().then((json) => {
                                document.getElementById("planTitle").innerText = "Generated text:";
                                document.getElementById("plan").innerText = json.data;
                                clearInterval(loadInterval);
                                document.getElementById("button").firstChild.nodeValue = "Submit";
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
        <div style={{ paddingTop: '4rem' }}>
            <h1 className='text-center'>Generate Sample Semester Plan!</h1>
            <p className='text-center' style={{fontSize: '20px'}}>
                Input advisor prompt below and press submit when ready!
                <br/>
                For the best results be specific, add info like current year/semester.
            </p>
            <MDBContainer className="p-3 my-5 d-flex flex-column w-25">

                <MDBTextArea wrapperClass='mb-4' placeholder='Enter text here!' id='prompt' type='text' />
                <MDBBtn className='mb-4' style={{ height: '2.4em' }} onClick={generatePlan} id='button' >Submit</MDBBtn>

            </MDBContainer>
            <h2 className='text-center' id='planTitle'></h2>
            <div style={{ paddingLeft: '20%' ,  paddingRight: '20%', whiteSpace: 'pre-wrap'}}>
                <p className='text-left' id='plan'></p>
            </div>
        </div>
    );
}

export default SemesterPlan;