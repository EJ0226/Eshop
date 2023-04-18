<template>
<div class="max-w-screen">
    <div class="w-full h-[50px] bg-[#F28383] flex">
      <img
        :src="searchSvg"
        alt="searchSvg"
        class="w-[30px] h-[30px] mt-[10px] ml-[10px]"
      />
      <input
        class="w-[200px] bg-[#F28383] border-4 border-[#FFFFFF] h-[30px] mt-[10px] rounded-xl ml-[10px] "
        placeholder="搜尋想查找的商品"
        required
        maxlength="30"
        v-model="searchkeyword"
      />
      <button
        class="w-[30px] h-[30px] mt-[10px] ml-auto"
        @click="goToShoppingCart"
      >
        <img :src="shoppingcartSvg" alt="shoppingcartSvg" />
      </button>
    </div>
    <div
      class="w-full h-[150px] bg-[#D9D9D9] mt-[25px] flex justify-center items-center"
    >
      <p class="font-black text-[40px] text-[#ffffff]">FHSH MARKET</p>
    </div>
    <div
      class="w-full mt-[25px] grid grid-cols-1 md:grid-cols-2 items-center justify-self-center gap-2 gap-y-8">
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

import searchSvg from "../assets/Search.svg"; //img
import shoppingcartSvg from "../assets/ShoppingCart.svg"; //img 我想一下img怎麼用 再測試
import Product from "../components/ProductUser.vue"; //跑版的product組件具體還要再測試

const request = axios.create({
  baseURL: "http://127.0.0.1:8000/api",
});
const products = ref([]); // 當前頁面顯示的商品資料
const searchKeyword = ref(""); // 搜尋關鍵字
const router = useRouter()

const fetchData = async () => {
  const data = {
    searchKeyword: searchKeyword.value,
  }
  await request.post("/api/products", data)
  .then((response) => {
  products.value = response.data;
})
.catch((error) => {
      console.log(error.response.data);
    });
  }
const goToShoppingCart = () => {
      router.push("/shoppingCart");
    }
</script>
