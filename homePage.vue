<template>
  <div class="max-w-screen">
    <div class="w-full h-[50px] bg-[#F28383] flex justify-start items-center">
      <img 
        @click="fetchData"
        :src="searchSvg"
        alt="searchSvg"
        class="w-[30px] h-[30px] mt-[10px] ml-[10px]"
      />
      <input
    class="w-[200px] h-[30px] mt-[10px] rounded-[10px] ml-[10px] border-4 border-[#FFFFFF] bg-[#F28383] text-center  placeholder-black"
    placeholder="搜尋想查找的商品"
    type="text"
    required
    maxlength="50"
    @keyup.enter="fetchData"
    v-model="searchKeyword"
    />
    <label class="mt-[13px] ml-[10px]">商品排序方式</label>
      <select v-model="sort_by" class="h-[30px] mt-[10px] ml-[2]">
        <option value="">請選擇</option>
        <option value="price_desc">價格降序</option>
        <option value="price_asc">價格升序</option>
      </select>
      <button
        @click="goToLogin"
        class="w-[70px] h-[30px] bg-[#ffffff] mr-[10px] mt-[10px] rounded-[10px]"
      >
        登入
      </button>
      <img
      
        :src="ShoppingCartsvg"
        alt="ShoppingCartsvg"
        class="w-[30px] h-[30px] mt-[10px] ml-[10px] flex  flex-col items-end"
      />
    </div>
    <div
      class="w-full h-[150px] bg-[#657099] mt-[25px] flex justify-center items-center"
    >
      <p class="font-black text-[40px] text-[#ffffff]">FHSH MARKET</p>
    </div>
    <div
      class="w-full mt-[25px] grid grid-cols-1 md:grid-cols-2 items-center justify-self-center gap-2 gap-y-8"
    >
      <Product
        v-for="product in products"
        :key="product.productName"
        :product="product.productName"
        :price="product.price"
      />
    </div>
  </div>
</template>

<script setup>
import axios from 'axios';
import { ref } from "vue";
import { useRouter } from "vue-router"
import searchSvg from "../assets/Search.svg";
import ShoppingCartsvg from "../assets/ShoppingCart.svg";
import Product from "../components/ProductUser.vue";
const request = axios.create({
  baseURL: "http://127.0.0.1:8000/api",
});
//把後端儲存好的商品資料顯示在網頁上(粗略)
const products = ref([]); // 當前頁面顯示的商品資料
const searchKeyword = ref(""); // 搜尋關鍵字
const sort_by = ref("price_desc")
const router = useRouter()

const fetchData = async () => {
  const data = {
    searchKeyword: searchKeyword.value,
    sort_by: sort_by.value,
  }
  await request.post("/products", data)
  .then((response) => {
  products.value = response.data;
})
.catch((error) => {
      console.log(error.response.data);
    });
  }
const goToLogin = () => {
      router.push("/login");
    }
</script>
