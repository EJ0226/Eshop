<script setup>
import Order from "../components/Order.vue";
import axios from 'axios';
import { ref } from "vue";
const Orders = ref([]);

</script>

<template>
  <div>
    <div
      class="w-screen h-[40px] bg-[#D9D9D9] font-thin text-[20px] flex justify-center items-center"
    >
      商品預約情況
    </div>
    <div class="mt-[20px]">
      <Order
        v-for="Order in Orders"
        :key="Order.num"
        :num="Order.num"
        :name="Order.name"
        :number="Order.number"
      />
    </div>
  </div>
</template>
