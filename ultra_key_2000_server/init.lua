local i = minetest.mod_channel_join("ultra_key_2000")

print("Server created/joined channel: ultra_key_2000")

local k_up = {}
local k_do = {}

local function ultra_receive_key_2000(channel_name, sender, message)
  if channel_name ~= "ultra_key_2000" then return end

  local key_up_acc = {}
  local key_do_acc = {}

  for r_k_dat in string.gmatch(message, '([^-&-]+)') do
    local k, v = r_k_dat:match("([^,]+)_([^,]+)")

    if (v == "up") then
      table.insert(key_up_acc, k)
    elseif (v == "down") then
      table.insert(key_do_acc, k)
    else
      error("fragmented data.")
    end
  end

  for _,v in ipairs(key_up_acc) do
    print("up: ", v)
  end
  for _,v in ipairs(key_do_acc) do
    print("down: ", v)
  end

  k_up = key_up_acc
  k_do = key_do_acc

  -- Then the external API would use those 2 arrays.
  --! But I'm not going to do that because this is not a solution and you should not be using this.
end

minetest.register_on_modchannel_message(ultra_receive_key_2000)
