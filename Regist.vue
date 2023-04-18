<template>
  <div class="w-screen h-screen flex flex-col items-center">
    <h1 class="font-black text-[40px] text-center mt-[60px]">註冊帳號</h1>
    <div class="mt-[60px]">
      <form @:submit.prevent="regist">
        <div>
          <label for="username">使用者名稱:</label>
          <input
            minlength="3"
            maxlength="20"
            type="text"
            placeholder="請輸入3-20個字符"
            class="w-[240px] h-[40px] bg-[#D9D9D9] text-center mb-[30px]"
            id="username"
            name="username"
            v-model.trim="formData.username"
            required
          />
        </div>
        <div>
          <label for="email">email:</label>
          <input
            minlength="3"
            maxlength="20"
            type="text"
            placeholder="請輸入3-20個字符"
            class="w-[240px] h-[40px] bg-[#D9D9D9] text-center mb-[30px]"
            id="email"
            name="email"
            v-model.trim = "formData.email"
            required
          />
        </div>
        <div>
          <label for="password">輸入密碼:</label>
          <input
            minlength="7"
            maxlength="16"
            type="password"
            placeholder="請輸入7-16個字符"
            class="w-[240px] h-[40px] bg-[#D9D9D9] text-center mb-[30px]"
            id="password"
            name="password"
            v-model.trim = "formData.password"
            required
          />
        </div>
        <div>
          <label for="checkpassword">確認密碼:</label>
          <br />
          <input
            minlength="7"
            maxlength="16"
            type="password"
            placeholder="請再次確認密碼"
            class="w-[240px] h-[40px] bg-[#D9D9D9] text-center mb-[30px]"
            id="check-password"
            name="checkpassword"
            v-model.trim = "formData.checkpassword"
            required
          />
        </div>
        <p v-if="password.value !== checkpassword.value">
          請確認密碼和確認密碼是否輸入正確
        </p>
        <!-- 需要加上一點設計 -->
        <div class="flex justify-center items-center mt-[30px]">
          <router-link class="router-link" to="/login">已有帳號</router-link>
          <!-- 待測試 -->
          <button
            type="submit"
            class="ml-[25px] w-[77px] h-[44px] bg-[#D9D9D9] rounded-[15px] text-[24px] flex justify-center items-center"
          >
            註冊
          </button>
        </div>
      </form>
    </div>
  </div>
</template>

<script setup>
import axios from "axios";
import { reactive } from "vue";

const request = axios.create({
  baseURL: "http://127.0.0.1:8000/api",
});

const formData = reactive({
  username: "",
  email: "",
  password: "",
  checkpassword: "",
});

const regist = async () => {
  const data = {
    username: formData.username,
    email: formData.email,
    password: formData.password,
    checkpassword: formData.checkpassword,
  };
  if (!username.value) {
    alert("請輸入使用者名稱");
    return;
  }
  if (!formData.email) {
    alert("請輸入email");
    return;
  }
  if (!fromData.password) {
    alert("請輸入密碼");
    return;
  }
  if (!fromData.checkassword) {
    alert("請輸入確認密碼");
    return;
  }
  if (fromData.password !== DfromData.checkpassword) {
    alert("請確認密碼和輸入密碼是否一致");
    return;
  }
  await request.post("/register", data)
    .then((response) => {
      //response.data => "id": str(result.inserted_id),"username": user["username"],"access_token": user["access_token"],
      router.push("/login");
      console.log(response.data)
    })
    .catch((error) => {
      console.log(error.response.data);
    });
};
</script>
<style>
.router-link {
  display: inline-block;
  padding: 8px 16px;
  border: 2px solid black;
  border-radius: 4px;
  text-decoration: none;
  font-size: 24px;
  font-weight: bold;
  color: black;
  width: 77px;
  height: 44px;
  background-color: #D9D9D9;
  border-radius: 15px;
  display: flex;
  justify-content: center;
  align-items: center;
}

.router-link:hover {
  background-color: black;
  color: white;
}
</style>