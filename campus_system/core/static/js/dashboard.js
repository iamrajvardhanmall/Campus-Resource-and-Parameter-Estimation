// Simple Campus Dashboard JavaScript

document.addEventListener('DOMContentLoaded', function() {
    console.log('Campus Dashboard loaded');
    
    // Add simple hover effects for stat cards
    const statCards = document.querySelectorAll('.stat-card');
    statCards.forEach(card => {
        card.addEventListener('mouseenter', function() {
            this.style.transform = 'translateY(-4px)';
        });
        
        card.addEventListener('mouseleave', function() {
            this.style.transform = 'translateY(0)';
        });
    });
    
    // Add simple row highlighting for tables
    const tableRows = document.querySelectorAll('tbody tr');
    tableRows.forEach(row => {
        row.addEventListener('mouseenter', function() {
            this.style.backgroundColor = '#f1f3f4';
        });
        
        row.addEventListener('mouseleave', function() {
            this.style.backgroundColor = '';
        });
    });
});