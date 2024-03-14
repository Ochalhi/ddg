describe('template spec', () => {
  it('user should be able to send a message', () => {
    cy.visit('http://localhost:8080')
    let currentTime = Date.now();
    cy.get('input[type="text"]').type('Hello duck, this is a test message at '+ currentTime)

    cy.get('button').contains('Submit').click()
    cy.contains('span', 'Hello duck, this is a test message at '+ currentTime).should('be.visible')
  })
})