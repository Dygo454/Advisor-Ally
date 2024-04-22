import React from 'react';

import {
    MDBNavbar,
    MDBNavbarNav,
    MDBNavbarItem,
    MDBNavbarLink,
    MDBContainer,
    MDBNavbarBrand
}
    from 'mdb-react-ui-kit';

function SemesterPlan() {

    return (
        <div>
            <MDBNavbar expand='sm' className='bg-body-tertiary'>
                <MDBContainer>
                    <MDBNavbarBrand>Advisor Ally</MDBNavbarBrand>
                        <MDBNavbarNav left fullWidth={false} className='navbar-items'>
                            <MDBNavbarItem>
                                <MDBNavbarLink href='/login'>Log out</MDBNavbarLink>
                            </MDBNavbarItem>
                        </MDBNavbarNav>
                </MDBContainer>
            </MDBNavbar>

            <h2 className='mt-5 mb-4 text-center' style={{ fontSize: '24px' }}>Your Semester Plan</h2>

            <MDBContainer className='p-3 my-5 d-flex flex-column w-75' style={{ border: '1px solid #ced4da', borderRadius: '0.25rem', boxShadow: '0 0.5rem 1rem regba(0, 0, 0, 0.15' }}>
                <h3 className='mb-4 text-center' style={{ fontSize: '18px' }}>Year 1</h3> 
            </MDBContainer>

            <MDBContainer className='p-3 my-5 d-flex flex-column w-75' style={{ border: '1px solid #ced4da', borderRadius: '0.25rem', boxShadow: '0 0.5rem 1rem regba(0, 0, 0, 0.15' }}>
                <h3 className='mb-4 text-center' style={{ fontSize: '18px' }}>Year 2</h3>
            </MDBContainer>

            <MDBContainer className='p-3 my-5 d-flex flex-column w-75' style={{ border: '1px solid #ced4da', borderRadius: '0.25rem', boxShadow: '0 0.5rem 1rem regba(0, 0, 0, 0.15' }}>
                <h3 className='mb-4 text-center' style={{ fontSize: '18px' }}>Year 3</h3>
            </MDBContainer>

            <MDBContainer className='p-3 my-5 d-flex flex-column w-75' style={{ border: '1px solid #ced4da', borderRadius: '0.25rem', boxShadow: '0 0.5rem 1rem regba(0, 0, 0, 0.15' }}>
                <h3 className='mb-4 text-center' style={{ fontSize: '18px' }}>Year 4</h3>
            </MDBContainer>

        </div>
    );
}

export default SemesterPlan;