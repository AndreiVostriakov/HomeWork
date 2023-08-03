function greeting() {
    const name_user = prompt('Введите своё имя');
    return name_user;
}

const user = greeting();
alert(`Здравствуйте, ${user}!`);
console.log(`Здравствуйте, ${user}!`);