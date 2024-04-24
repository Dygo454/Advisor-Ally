import React from 'react';
import { useNavigate } from 'react-router-dom';
import { useCookies } from 'react-cookie';
import './style.css';

import {
    MDBContainer,
    MDBBtn,
    MDBInput
}
    from 'mdb-react-ui-kit';

function Login() {
    const navigate = useNavigate();
    let shib="_shibsession_68747470733a2f2f73702e6c6f67696e2e75666c2e6564752f75726e3a6564753a75666c3a70726f643a30303734312f68747470733a2f2f73702e6c6f67696e2e75666c2e6564752f75726e3a6564753a75666c3a70726f643a30303734312f"
    let loading = false;
    const [_, setCookies] = useCookies(["access_token"])
    const useLoginResponse = async (resp) => {
        if (resp.status === 200) {
            let setCookie = document.cookie;
            let ind1 = setCookie.indexOf(shib)+shib.length+1;
            let ind2 = setCookie.indexOf(";", ind1);
            localStorage.setItem(shib, setCookie.substring(ind1,ind2));
            navigate("/info");
        }
        else if (resp.status === 401) {
            resp.json().then((json) => {
                alert(json.error);
            });
        }
        else {
            alert("An error occured with in server! Try again later.");
        }
        loading = false;
    }
    const handleLogin = () => {
        if (loading) {
            return;
        }
        loading = true;
        const postData = {
            'USERNAME': document.getElementById('USERNAME').value,
            'PASSWORD': document.getElementById('PASSWORD').value
        };
        const requestOptions = {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify(postData)
        };
        fetch("http://localhost:5000/login",requestOptions).then(useLoginResponse);
    }

    return (
        <div style={{ paddingTop: '4rem' }}>
            <p className='text-center' style={{ fontSize: '24px' }}>Welcome to Advisor Ally!</p>
            <p className='text-center' style={{ fontSize: '16px' }}>Sign in below with your ONE.UF login. (remember the duo push!)</p>
            <MDBContainer className="p-3 my-5 d-flex flex-column w-25">

                <MDBInput wrapperClass='mb-4' placeholder='Username' id='USERNAME' type='username' />
                <MDBInput wrapperClass='mb-4' placeholder='Password' id='PASSWORD' type='password' />

                <MDBBtn className='mb-4' style={{ height: '2.4em' }} onClick={handleLogin} >Sign in</MDBBtn>

            </MDBContainer>
        </div>
    );
}


export default Login;