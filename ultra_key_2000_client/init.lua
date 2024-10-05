--? Implementation note:
-- This never gets any messages from the server.
-- Any message received from this is from the stupid python script.

print("HELLO FROM CLIENT MOD!")

local m

minetest.register_on_modchannel_signal(function(c, signal)
  if c ~= "ultra_key_2000" then return end
  if signal ~= 0 then
    error("ultra_key_2000: channel join failure")
  end


  local function ultra_receive_key_2000(channel_name, sender, message)
    if channel_name ~= "ultra_key_2000" then return end
    if sender ~= "ultra_key_2000" then return end

    -- We received a spoofed message, now send it to the server for real.
    m:send_all(message)
  end

  minetest.register_on_modchannel_message(ultra_receive_key_2000)
end)

m = minetest.mod_channel_join("ultra_key_2000")
