import { Link, useNavigate } from 'react-router-dom';
import './style.css';

import {
    MDBContainer,
    MDBBtn,
    MDBInput
}
    from 'mdb-react-ui-kit';

function Signup() {
    const navigate = useNavigate();

    const handleSignup = () => {
        navigate('/info');
    }

  return (
      <div style={{ paddingTop: '4rem' }}>
          <h2 className='mb-4 text-center' style={{ fontSize: '24px' }}>Sign Up With Advisor Ally!</h2>
          <p className='text-center' style={{ fontSize: '18px' }}>An AI advisor that creates custom semester plans to students of any major at UF.</p>
          <MDBContainer className='p-3 my-5 d-flex flex-column w-25' style={{ border: '1px solid #ced4da', borderRadius: '0.25rem', boxShadow: '0 0.5rem 1rem regba(0, 0, 0, 0.15' }}>
              <h3 className='mb-4 text-center' style={{ fontSize: '18px' }}>Register</h3>

              <MDBInput wrapperClass='mb-4' placeholder='Name' id='form1' type='name' />
              <MDBInput wrapperClass='mb-4' placeholder='Email' id='form2' type='email' />
              <MDBInput wrapperClass='mb-4' placeholder='Password' id='form3' type='password' />
              <MDBInput wrapperClass='mb-4' placeholder='Confirm Password' id='form4' type='confirmpassword' />

              <button className='mb-4 custom-button' onClick={handleSignup}>Sign up</button>

               <div className="text-center">
                  <p>Already registered? <Link to='/login'>Log in</Link></p>
              </div>

          </MDBContainer>
      </div>
  );
}

export default Signup;