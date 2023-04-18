<template>
 <div class="min-h-screen bg-gray-50">
   <div class="bg-rose-400 relative w-full text-center" style="padding-top: 9%; padding: 40px;">
     <p class="text-4xl font-bold text-gray-50 leading-[77.45px]" style="font-family: 'Inter'; font-size: 64px;">購物車</p>
   </div>
   <div class="h-8 bg-white"></div>
    <div class="mt-6 mx-auto w-10/12">
      <cart-product class="mb-8"></cart-product>
      <cart-product class="mb-8"></cart-product>
    </div>
    <div class="h-8 bg-white"></div>
    <div class="bg-rose-400 h-24 flex justify-center items-center">
      <p class="text-3xl font-bold text-gray-50 mr-4">總金額{{count}}</p>
      <button class="w-64 h-16 bg-white font-bold text-xl">
        下單
      </button>
    </div>
  </div>
</template>

<script setup>
import CartProduct from "../components/Cart-Product.vue";
import { ref, reactive } from "vue";
const shoppingCart = ref([])
const conut = ref(0)
</script>
