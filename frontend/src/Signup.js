import React, { useState } from 'react';
import { Link, useNavigate } from 'react-router-dom';

import {
    MDBContainer,
    MDBTabs,
    MDBTabsItem,
    MDBTabsLink,
    MDBTabsContent,
    MDBTabsPane,
    MDBIcon,
    MDBCheckbox,
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
          <p className='text-center' style={{ fontSize: '24px' }}>Sign Up With Advisor Ally!</p>
          <MDBContainer className="p-3 my-5 d-flex flex-column w-25">

              <MDBInput wrapperClass='mb-4' placeholder='Name' id='form1' type='name' />
              <MDBInput wrapperClass='mb-4' placeholder='Email' id='form2' type='email' />
              <MDBInput wrapperClass='mb-4' placeholder='Password' id='form3' type='password' />
              <MDBInput wrapperClass='mb-4' placeholder='Re-enter Password' id='form4' type='reenterpassword' />
              
              <MDBBtn className='mb-4' onClick={ handleSignup }>Sign up</MDBBtn>
               <div className="text-center">
                  <p>Already registered? <Link to='/login'>Log in</Link></p>
              </div>

          </MDBContainer>
      </div>
  );
}

export default Signup;