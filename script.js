function gerarLink() {
    const taskid = document.getElementById('taskid').value;
    const modo = document.getElementById('modo').value;
    const resultElement = document.getElementById('res');

    if (!taskid || !modo) {
        resultElement.textContent = 'Por favor, preencha todos os campos.';
        return;
    }

    if (!taskid.startsWith('VT')) {
        resultElement.textContent = 'Ocorreu um erro, digite a task_id corretamente!';
        return;
    }

    let link;
    const modoPrefix = modo.slice(0, 2);
    if (modoPrefix === 'AT') {
        if (!modo.startsWith('AT')) {
            resultElement.textContent = 'Isso não é uma AT!';
            return;
        }
        link = `https://spx.shopee.com.br/#/mercadao/audit-list/at-to-detail?task_id=${taskid}&target_id=${modo}&audit_target_type=2`;
    } else if (modoPrefix === 'TO') {
        if (!modo.startsWith('TO')) {
            resultElement.textContent = 'Isso não é uma TO!';
            return;
        }
        link = `https://spx.shopee.com.br/#/mercadao/audit-list/at-to-detail?task_id=${taskid}&target_id=${modo}&audit_target_type=3`;
    } else {
        resultElement.textContent = 'Selecione uma opção válida! AT ou TO.';
        return;
    }

    if (link) {
        resultElement.innerHTML = `<a href="${link}" target="_blank">Acessar página</a>`;
    }
}
