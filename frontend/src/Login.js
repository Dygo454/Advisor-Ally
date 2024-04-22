import { Link, useNavigate } from 'react-router-dom';
import './style.css';

import {
    MDBContainer,
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
            <h2 className='mb-4 text-center' style={{ fontSize: '24px' }}>Welcome to Advisor Ally!</h2>
            <p className='text-center' style={{ fontSize: '18px' }}>An AI advisor that creates custom semester plans to students of any major at UF.</p>
            <MDBContainer className='p-3 my-5 d-flex flex-column w-25' style={{ border: '1px solid #ced4da', borderRadius: '0.25rem', boxShadow: '0 0.5rem 1rem regba(0, 0, 0, 0.15' }}>
                <h3 className='mb-4 text-center' style={{ fontSize: '18px' }}>Log In</h3>

                <MDBInput wrapperClass='mb-4' placeholder='Email' id='form1' type='email' />
                <MDBInput wrapperClass='mb-4' placeholder='Password' id='form2' type='password' />
                             
                <button className='mb-4 custom-button' onClick={ handleLogin }>Log in</button>

                <div className='text-center'>
                    <p>Not registered? <Link to='/signup'>Sign up</Link></p>
                </div>

            </MDBContainer>
            </div>
    );
}


export default Login;