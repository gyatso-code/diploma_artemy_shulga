const modalController = ({modal, btnOpen, btnClose, time = 300}) => { 
    const buttonElem = document.querySelector(btnOpen);
    const modalElem = document.querySelector(modal);

    const disableScroll = () => {
        document.documentElement.style.overflow = 'hidden';
        document.documentElement.style.paddingRight = `${
            window.innerWidth - document.documentElement.clientWidth
        }px`;
    };

    
    const enableScroll = () => {
        document.documentElement.style.overflow = '';
        document.documentElement.style.paddingRight = '';
    };


    modalElem.style.cssText = `
        display: flex;
        visibility: hidden;
        opacity: 0;
        transition: opacity ${time}ms ease-in-out;
    `;


    const closeModal = event => {
        const target = event.target;

        if(target === modalElem ||
            (btnClose && target.closest(btnClose)) ||
            event.code === 'Escape'
        ) {
            modalElem.style.opacity = 0;

            setTimeout(() => {
                modalElem.style.visibility = 'hidden';
                enableScroll();
            }, time);

            window.removeEventListener('keydown', closeModal);
        }
    }

    const openModal = () => {
        modalElem.style.visibility = 'visible';
        modalElem.style.opacity = 1;
        disableScroll();
        window.addEventListener('keydown', closeModal)
    };

    buttonElem.addEventListener('click', openModal);
    modalElem.addEventListener('click', closeModal);
};

modalController({
    modal: '.modal',
    btnOpen: '.btn',
    btnClose: '.modal__close'
});