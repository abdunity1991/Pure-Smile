// دالة لإضافة المنتج إلى السلة
let addToCartButtons = document.querySelectorAll('.add-to-cart');
addToCartButtons.forEach(button => {
    button.addEventListener('click', function() {
        alert('تم إضافة المنتج إلى السلة!');
        // إضافة منطق إضافة المنتج للسلة هنا
    });
});
