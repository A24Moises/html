async function fetchUsers() {
    try {
        const response = await fetch('https://api.slingacademy.com/v1/sample-data/users?offset=10&limit=20');
        if (!response.ok) throw new Error('Error en la petición');
        
        const data = await response.json();
        const users = data.users;
        
        const container = document.getElementById('userContainer');
        container.innerHTML = ''; // Limpiar el contenedor
        
        users.forEach(user => {
            const userCard = document.createElement('div');
            userCard.classList.add('user-card');
            userCard.innerHTML = `
                <img src="${user.profile_picture}" alt="Foto de ${user.first_name}">
                <h3>${user.first_name} ${user.last_name}</h3>
                <p>Email: ${user.email}</p>
                <p>Tel: ${user.phone}</p>
            `;
            container.appendChild(userCard);
        });

    } catch (error) {
        console.error('Error:', error);
    }
}


