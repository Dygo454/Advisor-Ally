import React, { useState } from 'react';
import { Link, useNavigate } from 'react-router-dom';
import './style.css';

import {
    MDBContainer,
    MDBBtn,
    MDBInput
}
    from 'mdb-react-ui-kit';


function Login() {
    const navigate = useNavigate();

    const handleLogin = () => {
        navigate('/plan');
    }

    return (
        <div style={{ paddingTop: '4rem' }}>
            <p className='text-center' style={{ fontSize: '24px' }}>Welcome to Advisor Ally!</p>
            <MDBContainer className="p-3 my-5 d-flex flex-column w-25">

                <MDBInput wrapperClass='mb-4' placeholder='Email' id='form1' type='email' />
                <MDBInput wrapperClass='mb-4' placeholder='Password' id='form2' type='password' />

                <MDBBtn className='mb-4' onClick={handleLogin} >Sign in</MDBBtn>
                <br />

                <div className="text-center">
                    <p>Not registered? <Link to='/signup'>Sign up</Link></p>
                </div>

            </MDBContainer>
        </div>
    );
}


export default Login;