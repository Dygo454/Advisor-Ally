import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';

import {
    MDBContainer
}
    from 'mdb-react-ui-kit';

function Info() {

    const [selectedValue, setSelectedValue] = useState('');

    const handleSelectChange = (event) => {
        setSelectedValue(event.target.value);
    };

    const navigate = useNavigate();

    const handleContinue = () => {
        navigate('/plan');
    }

    return (
        <>
            <div style={{ paddingTop: '4rem' }}>
                <h2 className='mb-4 text-center' style={{ fontSize: '24px' }}>Welcome to Advisor Ally!</h2>
                <p className='text-center' style={{ fontSize: '18px' }}>Answer the following questions to have your semester plan created.</p>

                {/* 
                <MDBContainer className='p-3 my-5 d-flex flex-column w-50' style={{ border: '1px solid #ced4da', borderRadius: '0.25rem', boxShadow: '0 0.5rem 1rem regba(0, 0, 0, 0.15' }}>
                    <div>
                        <label htmlFor='my-dropdown' style={{ marginRight: '10px' }}>Select an option</label>
                        <select id='my-dropdown' value={ selectedValue } onChange={ handleSelectChange }>
                            <option value=''></option>
                            <option value='option1'>option 1</option>
                            <option value='option2'>option 2</option>
                        </select>
                    </div>
                </MDBContainer>
                */}

                <div style={{ display: 'flex', justifyContent: 'center', alignItems: 'center', height: '100vh'}} >
                    <button className='mt-4 mb-4 custom-button' onClick={ handleContinue }>Continue</button>
                </div>


            </div>
        </>
    );
}

export default Info;