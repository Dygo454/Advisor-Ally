import React from 'react';
import { useNavigate } from 'react-router-dom';
import './style.css';

import {
    MDBContainer,
    MDBNavbar,
    MDBNavbarNav,
    MDBNavbarItem,
    MDBNavbarLink,
    MDBNavbarBrand
}
    from 'mdb-react-ui-kit';
import { useEffect } from 'react';

function SemesterPlan() {
    let navigate = useNavigate();
    const shib="_shibsession_68747470733a2f2f73702e6c6f67696e2e75666c2e6564752f75726e3a6564753a75666c3a70726f643a30303734312f68747470733a2f2f73702e6c6f67696e2e75666c2e6564752f75726e3a6564753a75666c3a70726f643a30303734312f";
    let signout = () => {
        localStorage.removeItem(shib);
        localStorage.removeItem("data");
        navigate("/login")
    };
    let onLoad = () =>{
        let data = localStorage.getItem("data");
        let firstFound = false;
        for (let i = 1; i < 6; i++) {
            let ind = data.indexOf("Year "+i+":");
            if (ind < 0) {
                continue;
            } else if (ind != 0 && !firstFound) {
                localStorage.setItem("data","Year "+i-1+":\n"+data);
                onLoad();
                return;
            }
            firstFound = true;
            ind += 8;
            let ind2 = data.indexOf("Year "+(i+1)+":");
            if (ind2 < 0) {
                ind2 = data.length;
            }
            let currStr = data.substring(ind,ind2);
            document.getElementById("y"+i+"Data").innerText = currStr;
        }
    };
    useEffect(onLoad);
    return (
        <div>
            <MDBNavbar expand='sm' className='bg-body-tertiary'>
                <MDBContainer>
                    <MDBNavbarBrand>Advisor Ally</MDBNavbarBrand>
                        <MDBNavbarNav left fullWidth={false} className='navbar-items'>
                            <MDBNavbarItem>
                                <MDBNavbarLink onClick={signout}>Log out</MDBNavbarLink>
                            </MDBNavbarItem>
                        </MDBNavbarNav>
                </MDBContainer>
            </MDBNavbar>

            <h2 className='mt-5 mb-4 text-center' style={{ fontSize: '24px' }}>Your Semester Plan</h2>

            <MDBContainer id='y1' className='p-3 my-5 d-flex flex-column w-75' style={{ border: '1px solid #ced4da', borderRadius: '0.25rem', boxShadow: '0 0.5rem 1rem regba(0, 0, 0, 0.15', whiteSpace: 'pre-wrap' }}>
                <h3 className='mb-4 text-center' style={{ fontSize: '18px' }}>Year 1</h3>
                <p id='y1Data'></p>
            </MDBContainer>

            <MDBContainer id='y2' className='p-3 my-5 d-flex flex-column w-75' style={{ border: '1px solid #ced4da', borderRadius: '0.25rem', boxShadow: '0 0.5rem 1rem regba(0, 0, 0, 0.15', whiteSpace: 'pre-wrap' }}>
                <h3 className='mb-4 text-center' style={{ fontSize: '18px' }}>Year 2</h3>
                <p id='y2Data'></p>
            </MDBContainer>

            <MDBContainer id='y3' className='p-3 my-5 d-flex flex-column w-75' style={{ border: '1px solid #ced4da', borderRadius: '0.25rem', boxShadow: '0 0.5rem 1rem regba(0, 0, 0, 0.15', whiteSpace: 'pre-wrap' }}>
                <h3 className='mb-4 text-center' style={{ fontSize: '18px' }}>Year 3</h3>
                <p id='y3Data'></p>
            </MDBContainer>

            <MDBContainer id='y4' className='p-3 my-5 d-flex flex-column w-75' style={{ border: '1px solid #ced4da', borderRadius: '0.25rem', boxShadow: '0 0.5rem 1rem regba(0, 0, 0, 0.15', whiteSpace: 'pre-wrap' }}>
                <h3 className='mb-4 text-center' style={{ fontSize: '18px' }}>Year 4</h3>
                <p id='y4Data'></p>
            </MDBContainer>

        </div>
    );
}

export default SemesterPlan;