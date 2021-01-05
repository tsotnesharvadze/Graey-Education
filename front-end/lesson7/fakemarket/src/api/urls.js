const urls = {
    productListing: 'https://fakestoreapi.com/products',
    productDetail: (id) => `https://fakestoreapi.com/products/${id}`,
    categories: 'https://fakestoreapi.com/products/categories',
    filterByCategory: (categorySlug) => `https://fakestoreapi.com/products/category/${categorySlug}`,
};

export default urls