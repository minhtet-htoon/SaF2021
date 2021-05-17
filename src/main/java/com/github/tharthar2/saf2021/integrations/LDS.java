package com.github.tharthar2.saf2021.integrations;


import com.oblivioussp.spartanweaponry.api.WeaponMaterial;
import com.oblivioussp.spartanweaponry.api.trait.MeleeCallbackWeaponTrait;
import net.minecraft.entity.Entity;
import net.minecraft.entity.EntityType;
import net.minecraft.entity.LivingEntity;
import net.minecraft.entity.effect.LightningBoltEntity;
import net.minecraft.entity.player.PlayerEntity;
import net.minecraft.item.ItemStack;


public class LDS extends MeleeCallbackWeaponTrait {


    public LDS(String propType, String propModId, TraitQuality quality) {
        super(propType, propModId, quality);
    }

    public void onHitEntity(WeaponMaterial material, ItemStack stack, LivingEntity target,
                            LivingEntity attacker, Entity projectile) {
        boolean flag = true;
        if(attacker instanceof PlayerEntity){
            if(((PlayerEntity)attacker).swingProgress > 0.2){
                flag = false;
            }
        }
        if(!attacker.world.isRemote && flag){
            LightningBoltEntity lightningboltentity = EntityType.LIGHTNING_BOLT.create(target.world);
            assert lightningboltentity != null;
            lightningboltentity.moveForced(target.getPositionVec());
            if(!target.world.isRemote){
                target.world.addEntity(lightningboltentity);
            }
        }
        target.applyKnockback( 1F, attacker.getPosX() - target.getPosX(), attacker.getPosZ() - target.getPosZ());
    }
}

